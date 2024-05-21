L = input()

l = len(L)
sum = 10
for i in range(0,l-1):
    if L[i] == L[i+1]:
        sum += 5
    else:
        sum += 10
print(sum)