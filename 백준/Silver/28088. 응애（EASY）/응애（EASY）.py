from collections import deque
deq = deque()

N, M, K, *L = list(map(int,open(0).read().split()))

babyL = [False for i in range(N)]

for i in range(M):
  babyL[L[i]] = True

count = 0
while count < K:
  for i in range(len(babyL)):
    if babyL[i] == True:
      deq.append(i)
  while deq:    
        i = deq.popleft()
        if i == 0:
          babyL[N-1] = not babyL[N-1]
          babyL[0] = not babyL[0]
          babyL[1] = not babyL[1]
        elif i == N-1:
          babyL[N-2] = not babyL[N-2]
          babyL[N-1] = not babyL[N-1]
          babyL[0] = not babyL[0]
        else:
          babyL[i-1] = not babyL[i-1]
          babyL[i] = not babyL[i]
          babyL[i+1] = not babyL[i+1]
  count += 1
print(babyL.count(True))
