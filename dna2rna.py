# Python Stronghold
# transcribing DNA to RNA

file = open('/home/guy/Downloads/rosalind_rna.txt', 'r')
data = file.read()
data = data.strip()

RNA = data.replace('T', 'U')

print(RNA)
