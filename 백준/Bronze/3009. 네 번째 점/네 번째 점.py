L = list(map(int,open(0).read().split()))

dicx = {}
dicy = {}
answerX = 0
answerY = 0
for i in range(len(L)//2):
  if L[2*i] not in dicx:
    dicx[L[2*i]] = 1
  else: 
    dicx[L[2*i]] += 1
  if L[2*i+1] not in dicy:
    dicy[L[2*i+1]] = 1
  else: 
    dicy[L[2*i+1]] += 1

for x in dicx.keys():
  if dicx[x] == 1:
    answerX = x

for y in dicy.keys():
  if dicy[y] == 1:
    answerY = y
print(f"{answerX} {answerY}")
    