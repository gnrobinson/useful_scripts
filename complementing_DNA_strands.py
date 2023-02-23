# Python stronghold
# complementing DNA strands

file = open('/home/guy/Downloads/rosalind_rna.txt', 'r')
data = file.read()
data = data.strip()

def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])

def reverse_complement(dna):
  complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
  rc = ""
  for base in dna:
    rc += complement[base]
  return "".join(reversed(rc))
