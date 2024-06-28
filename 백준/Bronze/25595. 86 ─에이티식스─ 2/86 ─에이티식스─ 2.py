
n, *L = open(0).read().strip().split("\n")
for i in range(int(n)):
  L[i] = list(map(int,L[i].split()))
  
enemyList = []
start = (0,0)

for i in range(int(n)):
  for j in range(int(n)):
    if L[i][j] == 1:
      enemyList.append((i,j))
    elif L[i][j] == 2:
      start = (i,j)

sy,sx = start
answer = "Lena"

for ey,ex in enemyList:
  if sy % 2 == 0 and sx % 2 == 0:
    if ey % 2 == 0 and ex % 2 == 1:
      pass
    elif ey % 2 == 1 and ex % 2 == 0:
      pass
    else:
      answer = "Kiriya"
  elif sy % 2 == 1 and sx % 2 == 1:
    if ey % 2 == 0 and ex % 2 == 1:
      pass
    elif ey % 2 == 1 and ex % 2 == 0:
      pass
    else:
      answer = "Kiriya"
  elif sy % 2 == 0 and sx % 2 == 1:
    if ey % 2 == 0 and ex % 2 == 0:
      pass
    elif ey % 2 == 1 and ex % 2 == 1:
      pass
    else:
      answer = "Kiriya"
  elif sy % 2 == 1 and sx % 2 == 0:
    if ey % 2 == 0 and ex % 2 == 0:
      pass
    elif ey % 2 == 1 and ex % 2 == 1:
      pass
    else:
      answer = "Kiriya"

print(answer)