L = list(map(int,open(0).read().split()))

dic = {}

for l in L:
    i = l % 42
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    
print(len(dic.keys()))