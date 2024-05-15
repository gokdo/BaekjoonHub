N, *L = list(map(int,open(0).read().split()))
L.sort(reverse = True)

sum = 0
for i in range(1,N+1):
    sum += L[i-1] * i
print(sum)