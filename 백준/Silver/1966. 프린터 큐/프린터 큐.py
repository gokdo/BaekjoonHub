import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
  N,M = map(int,sys.stdin.readline().split())
  p = list(map(int,sys.stdin.readline().split()))
  dq = deque([])

  for i in range(N): # dq 초기화
    dq.append(i)
  pivot = 0
  
  while pivot < N:
    count = 0
    for j in range(pivot+1,N):
      if p[dq[pivot]] < p[dq[j]]:
         temp = dq[pivot]
         dq.remove(temp)
         dq.append(temp)
      else:
        count += 1
    if count == N - (pivot+1):
      pivot += 1
  print(dq.index(M)+1)