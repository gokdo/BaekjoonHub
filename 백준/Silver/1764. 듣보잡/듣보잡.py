from collections import Counter

N,M,*Data = list(open(0).read().split())

noHearList = []
noSeeList = []
sumList = []

for i in range(int(N)):
  noHearList.append(Data[i])
for i in range(int(N),int(N)+int(M)):
  noSeeList.append(Data[i])

counterHear = Counter(noHearList)
counterSee = Counter(noSeeList)
counterSum = counterHear + counterSee

for x in counterSum.items():
  if x[1] == 2:
    sumList.append(x[0])

print(len(sumList))
sumList.sort()
for y in sumList:
  print(y)