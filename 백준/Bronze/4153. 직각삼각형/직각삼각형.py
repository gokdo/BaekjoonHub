L = list(map(int,open(0).read().split()))

M = 0
sum = 0

for i in range(len(L)//3):
  if L[3*i] == 0:
    break
  else:
    M = max(L[3*i],L[3*i+1],L[3*i+2])
    for l in [L[3*i],L[3*i+1],L[3*i+2]]:
      if l != M:
        sum += l**2
    if sum == M**2:
      print("right")
    else:
      print("wrong")
    sum = 0