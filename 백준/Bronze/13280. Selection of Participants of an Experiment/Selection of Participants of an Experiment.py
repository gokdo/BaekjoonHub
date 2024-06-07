while 1:
  n = int(input())
  if n == 0:
    break
  else:
    L = []
    Data = list(map(int,input().split()))
    Data.sort()
    for i in range(1, n):
      L.append(Data[i] - Data[i-1])
    L.sort()
    print(L[0])