# rosalind Stronghold
# finding a motif in DNA

file = open("/home/guy/Downloads/rosalind_motif.txt", 'r')
dna = file.readline()
motif = file.readline()
dna = dna.strip()
motif = motif.strip()

string_list = [dna[i:i+len(motif)] for i in range(0, len(dna), 1)]

for i, j in enumerate(string_list):
  if j == motif:
    print(i+1)
