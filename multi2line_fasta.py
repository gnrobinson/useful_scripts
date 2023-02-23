with open("/home/guy/Downloads/rosalind_cons.txt", "r") as f, open ("/home/guy/Downloads/test.txt", "w") as output :
    seq =""
    for line in f :
        if line.startswith(">"):
            if seq != "":
                output.write(seq)
                seq=""
            seq += '\n'+line     
        else:
            seq += line.strip().replace('\n', '')
    else:
        #end of lines 
         if seq != "":
                output.write(seq)
                seq=""
