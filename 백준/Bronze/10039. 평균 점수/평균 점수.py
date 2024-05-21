L = list(map(int,open(0).read().split()))
sum = 0
for i in L:
   if i < 40:
    sum += 40
   else:
    sum += i
print(sum//len(L))
    