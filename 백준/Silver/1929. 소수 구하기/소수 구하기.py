import math
N,M = map(int,input().split())
count = [True for i in range(M+1)]

for i in range(2,M+1):
  if count[i] == True:
    for j in range(i+i,M+1,i):
        count[j] = False

for n in range(N):
  count[n] = False

count[0] = False
count[1] = False

for l in range(N,M+1):
  if count[l] == True:
    print(l)