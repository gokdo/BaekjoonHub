L = list(map(int,input().split()))

sum = 0

for l in L:
  sum += l**2

print(f"{sum%10}")