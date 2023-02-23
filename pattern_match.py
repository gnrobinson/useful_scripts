#!/usr/bin/python3

# pattern_match.py
# pattern match user specified columns from different files
# author: Guy Robinson

#importing required libraries
import argparse
import subprocess

def main():
    # interpret Argparse variables
    args = mainArgs()
    # open a user specified file
    query = open_user_file(args.query)
    subject = open_user_file(args.subject)
    # read file and make list
    lines_q = file_to_lines(query)
    lines_s = file_to_lines(subject)
    # split lists
    column_q = split_lines(lines_q)
    column_s = split_lines(lines_s)
    # match two files by column
    outfile = query_subject(column_q, column_s, args.column_query, args.column_subject)
    #readout list as tab-separated .txt file
    output_name = args.out + ".csv"
    list2output(outfile, output_name)
    #removes trailing commas (using sed)
    subprocess.call(["sed -i 's/,$//g' " + output_name], shell=True)

#defining required inputs
def mainArgs():
    parser = argparse.ArgumentParser(description='Pattern matches between user specified columns from a query file and subject file',prog='pattern-match')
    # Input options
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--subject',type=str,required=True)
    parser.add_argument('--column_query',type=int,required=True)
    parser.add_argument('--column_subject',type=int,required=True)
    # Output options
    parser.add_argument('--out',type=str,default=None,required=False,help='Use this prefix for output files. Default: None.')
    args = parser.parse_args()
    return args

# open files
def open_user_file(filename):
  #  filename = input("Filename: ") # for running without Argparse
    infile = open(filename,"r")
    return infile

# splits lines
def file_to_lines(infile):
    lines = []
    for line in infile:
        line = line.strip()
        lines.append(line)
    return lines

# splits each line into list of columns
def split_lines(lines):
    columns = []
    for line in lines:
        line_column = line.split()
        columns.append(line_column)
    return columns

# matches entry from column in query to subject column
# note it will output a filtered version of the subject file + query file
def query_subject(query, subject, q_col, s_col):
    q_col = q_col-1
    s_col =s_col-1
    i = 0
    matched_list = []
    while i < len(subject):
        search = subject[i][s_col]
        for sublist in query:
            if sublist[q_col] == search:
                matched_list.append(subject[i]+sublist)
        i += 1
    return matched_list

# reads out filtered subject list
def list2output(out_list, output_name):
    with open(output_name,'w') as f:
        for sublist in out_list:
            for item in sublist:
                f.write(item + ',')
            f.write('\n')

main()
