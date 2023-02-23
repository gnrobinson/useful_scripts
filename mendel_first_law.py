# python Stronghold
# Mendel's first law

file = open("/home/guy/Downloads/rosalind_iprb.txt", 'r')
data = file.read()
data = data.strip()
data = data.split(" ")

homo_dom = float(data[0])
hetero = float(data[1])
homo_recess = float(data[2])
total = homo_dom + hetero + homo_recess

homo_domTotal = homo_dom/total
heterTotal = ((hetero/total)*(homo_dom/(total-1))) + (((hetero/total)*((hetero-1)/(total-1)))*0.75) + (((hetero/total)*(homo_recess/(total-1)))*0.5)
homo_recessTotal = ((homo_recess/total)*(homo_dom/(total-1))) + (((homo_recess/total)*(hetero/(total-1)))*0.5)

ans = homo_domTotal + heterTotal + homo_recessTotal
print(ans)
