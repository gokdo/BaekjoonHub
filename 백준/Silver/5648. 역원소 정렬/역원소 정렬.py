n, *L = open(0).read().split()
for i in range(int(n)):
    L[i] = int(L[i].rstrip("0")[::-1])
L.sort()
for i in range(int(n)):
  print(L[i])