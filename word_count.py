# word_count.py
# Count the number of unique words in a file
# Author: Guy Robinson
def main():
    # open a user specified file
    infile = open_user_file()
    # read file and make list
    lines = file_to_lines(infile)
    print("Number of lines:",len(lines))
    # split list
    words = split_lines(lines)
    print("Number of words:", len(words))
    # make unique list
    # uniq_words = unique(words)
    # print("Number of unique words:", len(uniq_words))

    # Additional Function
    # Get the number of times a query word appears
    get_count_for_query(words)
    
def print_word_count_stats(word_counts):
    print("Total words:", sum(word_counts.values()))
    print("Number of distinct words:", len(word_counts))
    print("Min word count:", min(word_counts.values()))
    print("Max word count:", max(word_counts.values()))
    return

# open_user_file asks the user for a filename
# and opens it for reading returning the open
# filehandle
def open_user_file():
    filename = input("Enter filename:")
    infile = open(filename,"r")
    return infile

# file_to_lines reads a filehandle
# and returns a list of the lines of
# text in the file as strings
def file_to_lines(infile):
    lines = []
    
    for line in infile:
        line = line.strip()
        lines.append(line)
        
    return lines

# split_lines converts a list of lines to words by
# splitting each line on whitespace characters
def split_lines(lines):
    words = []
    for line in lines:
        line_words = line.split()
        for word in line_words:
            words.append(word)
            
    return words

# unique takes a list of potentially duplicated items
# and creates a new list where every item appears only
# once. E.g. ['one','one','two'] becomes ['one','two']
def unique(words):
    uniq_words = []
    for word in words:
        if word not in uniq_words:
            uniq_words.append(word)
    return uniq_words

def get_count_for_query(words):
    query = input("Enter a word:")
    count = words.count(query)
    print("Count:", count)

main()

