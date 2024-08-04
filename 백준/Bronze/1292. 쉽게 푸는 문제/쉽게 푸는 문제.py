a,b = map(int,input().split())
L = []
for i in range(1,1001):
    for j in range(i):
        L.append(i)
    
sum = 0
for i in range(a-1,b):
    sum += L[i]
print(sum)