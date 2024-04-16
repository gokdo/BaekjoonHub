N, *L = list(open(0).read().split())

LL = sorted(set(L), key = lambda x :(len(x),x))

for s in LL:
  print(s)