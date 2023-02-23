# Python stronghold
# counting CG content
# lines can't be wrapped though

file = open("/home/guy/Downloads/rosalind_fib2.txt", 'r')

def gc_content(str):
    for line in str
    gc = str.count("G") + str.count("C")
    return float(100*gc / len(str))

for line in file:
	line = line.strip()
	if '>' in line:
		print(line.lstrip(">"))
	else:
		print(gc_content(line))
