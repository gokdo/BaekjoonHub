N = int(input())
L = list(map(int,input().split()))
T, P = map(int,input().split())

tCount = 0
for i in range(6):
  tmp = L[i]
  while tmp > 0:
    tmp -= T
    tCount += 1

pCount = 0
while N >= 0:
  N -= P
  pCount += 1

pCount -= 1
N += P

print(tCount)
print(f"{pCount} {N}")