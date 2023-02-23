# python stronghold
# counting point mutations

file = open("/home/guy/Downloads/rosalind_hamm.txt", 'r')

s1 = file.readline()
s2 = file.readline()
s1 = s1.strip()
s2 = s2.strip()

def count_point(a, b)
  hamming = 0
  for x, y in zip(a, b):
    if x != y:
      hamming += 1
  return hamming

print(count_point(s1, s2))
