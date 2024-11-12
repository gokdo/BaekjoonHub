L, A, B, C, D = list(map(int,open(0).read().split()))

i = 0
while B > 0 or A > 0:
  A -= C
  B -= D
  i += 1
print(L-i)