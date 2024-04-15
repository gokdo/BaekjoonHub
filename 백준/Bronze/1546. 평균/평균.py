_, *L= list(map(int,open(0).read().split()))

M = max(L)
l = len(L)
sum = 0

for i in L:
    sum += round(i/M*100,2)
print(sum/l)
    
    
