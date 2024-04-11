def add(x,y):
  return x + y

data = list(map(int, open(0).read().split()))

row = data[0]
col = data[1]

listA = data[2 : row*col+2]
listB = data[row*col+2:]
answerList = list(map(add,listA,listB))
i = 0

dlist = []

for r in range(row):
    dlist.append([])
    for c in range(col):
        dlist[r].append(answerList[i])
        i += 1
        
for r in range(row):
    for c in range(col):
        print(dlist[r][c], end=" ")
    print()