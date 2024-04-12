T, *L = list(open(0).read().split())
for l in L:
  print(l[0]+l[len(l)-1])