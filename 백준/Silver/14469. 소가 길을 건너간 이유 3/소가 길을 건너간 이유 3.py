n, *L = list(map(int,open(0).read().split()))
nn = n
dic = {}
for i in range(n):
  if L[2*i] in dic:
    dic[L[2*i]] += L[2*i+1]
    nn -= 1
  else:
    dic[L[2*i]] = L[2*i+1]
nextEnter = 0
count = 0
for k, v in sorted(dic.items()):
    count += 1
    if nextEnter > k :
        nextEnter = nextEnter + v
    else:
        nextEnter = k + v
    
    if count == nn:
        print(nextEnter) 