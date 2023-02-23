# Python stronghold
# calculate number of nucleotides

file = open('/home/guy/Documents/Class/rosalind/rosalind_ini6.txt', 'r')
nuc_seq = file.read()
nuc_seq = nuc_seq.strip()

def count_nuc(str):
	count = dict()
	for letter in str:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
	return count

count_dict = count_nuc(nuc_seq)

for key, value in count_dict.items():
  print(value)
