T, *L = list(map(int,open(0).read().split()))

for i in range(0,len(L)):
  if i % 2 == 0:
    print(f"{L[i]+L[i+1]}")