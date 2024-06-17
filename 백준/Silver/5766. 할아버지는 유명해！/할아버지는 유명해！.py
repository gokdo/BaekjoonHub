from collections import Counter

while 1:
  N,M = map(int,input().split())
  if N == 0 and M == 0:
    break
  L = []
  for _ in range(N):
    L.extend(list(map(int,input().split())))
  mostCounter = Counter(L).most_common()
  counterList = []
  for i in range(len(mostCounter)):
    if mostCounter[i][1] not in counterList:
      counterList.append(mostCounter[i][1])
    else:
      pass
  counterList.sort(reverse=True)
  printList = []
  if len(counterList)>1:
    for mC in mostCounter:
      if mC[1] == counterList[1]:
        printList.append(mC[0])
  else:
    for mC in mostCounter:
      if mC[1] == counterList[0]:
        printList.append(mC[0])
  printList.sort()
  print(*printList)