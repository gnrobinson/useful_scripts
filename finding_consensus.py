# rosalind stronghold
# consensus and profile

file = open("/home/guy/Downloads/test.txt", 'r').read()
file = file.strip()
file = file.split('/n')

name = []
seq = []

def altElement(a):
	return a[1::2]

strings = altElement(f)

matrix = []
for i in strings:
	matrix.append([j for j in i])

# https://stackoverflow.com/questions/38586800/python-multiple-consensus-sequences

n = len(seq[0])
profile = { 'T':[0]*n,'G':[0]*n ,'C':[0]*n,'A':[0]*n }
for seq in matrix:
    for i, char in enumerate(seq):
        profile[char][i] += 1

for key, value in profile.items():
  print(key,':', " ".join([str(x) for x in value] ))

bestseqs = [[]]
for i in range(n):
    d = {N:profile[N][i] for N in ['T','G','C','A']}
    m = max(d.values())
    l = [N for N in ['T','G','C','A'] if d[N] == m]
    bestseqs = [ s+[N] for N in l for s in bestseqs ]

for s in bestseqs:
    print(''.join(s))
