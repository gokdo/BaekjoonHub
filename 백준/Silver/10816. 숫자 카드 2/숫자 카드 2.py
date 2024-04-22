N,NS,M,MS = open(0).read().strip().split("\n")

dic = {}
NL=list(map(int, NS.split()))
ML=list(map(int, MS.split()))

for i in NL:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
    
results = []
for j in ML:
    results.append(f"{dic.get(j,0)}")
    
print(*results)