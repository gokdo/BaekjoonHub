n, *L = list(map(int,open(0).read().split()))
sum = 0
for _ in range(n-1):
  a = min(L)
  del L[L.index(min(L))]
  b = min(L)
  del L[L.index(min(L))]
  L.append(a+b)
  sum += a*b
print(sum)