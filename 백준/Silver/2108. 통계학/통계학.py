from collections import Counter
N, *L = list(map(int,open(0).read().split()))

print(round(sum(L)/N))
sorted_L = sorted(L)
print(sorted_L[N//2])
if N>1:
  counterM = Counter(L).most_common()
  if counterM[0][1] == counterM[1][1]:
    itemSorter = []
    for i in range(len(counterM)):
      if counterM[i][1] == counterM[0][1]:
        itemSorter.append(counterM[i][0])
      else:
        break
    itemSorter.sort()
    print(itemSorter[1])
  else:
    print(counterM[0][0])
else:
  print(L[0])
print(max(L)-min(L))