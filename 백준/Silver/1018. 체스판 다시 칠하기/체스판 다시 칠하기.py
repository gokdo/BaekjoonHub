N,M,*L = list(open(0).read().strip().split())

lootW = {"start" : 65}
lootB = {"start" : 65}

for i in range(0,int(N)-7):
  for j in range(0,int(M)-7):
      lootW[f"{i},{j}"] = 0
      for ii in range(8):
        for jj in range(8):
          if ii % 2 == 0:
            if jj % 2 == 0:
              if L[i+ii][j+jj] == 'W':
                lootW[f"{i},{j}"] += 0
              else:
                lootW[f"{i},{j}"] += 1
            elif jj % 2 == 1:
              if L[i+ii][j+jj] == 'B':
                lootW[f"{i},{j}"] += 0
              else:
                lootW[f"{i},{j}"] += 1
          elif ii % 2 == 1:
            if jj % 2 == 0:
              if L[i+ii][j+jj] == 'B':
                lootW[f"{i},{j}"] += 0
              else:
                lootW[f"{i},{j}"] += 1
            elif jj % 2 == 1:
              if L[i+ii][j+jj] == 'W':
                lootW[f"{i},{j}"] += 0
              else:
                lootW[f"{i},{j}"] += 1
      lootB[f"{i},{j}"] = 0
      for ii in range(8):
        for jj in range(8):
          if ii % 2 == 0:
            if jj % 2 == 0:
              if L[i+ii][j+jj] == 'B':
                lootB[f"{i},{j}"] += 0
              else:
                lootB[f"{i},{j}"] += 1
            elif jj % 2 == 1:
              if L[i+ii][j+jj] == 'W':
                lootB[f"{i},{j}"] += 0
              else:
                lootB[f"{i},{j}"] += 1
          elif ii % 2 == 1:
            if jj % 2 == 0:
              if L[i+ii][j+jj] == 'W':
                lootB[f"{i},{j}"] += 0
              else:
                lootB[f"{i},{j}"] += 1
            elif jj % 2 == 1:
              if L[i+ii][j+jj] == 'B':
                lootB[f"{i},{j}"] += 0
              else:
                lootB[f"{i},{j}"] += 1
                
mW = min(lootW.values())
mB = min(lootB.values())

if mW == 65 and mB == 65:
  print(0)
else:
  print(min(mW,mB))