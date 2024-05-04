import sys

N = int(sys.stdin.readline().strip())
list = [0 for _ in range(10001)]
sumS = ""
for n in range(N):
    i = int(sys.stdin.readline().strip())
    list[i] += 1

for j in range(1,10001):
  if list[j] > 0:
    for jj in range(list[j]):
        print(j)
