N = int(input())

dic = {1:1}
i=0
n=0
pandan = 0
while pandan<N:
    i += 1
    dic[i] = 1+ 6*(n)
    pandan = dic[i]
    n += i
print(i)