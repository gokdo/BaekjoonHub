N, M = map(int,input().split())
L = []
answer = "Eyfa"
for i in range(N):
  L.append([])
  L[i] = list(input())
for i in range(N):
  word = ""
  for j in range(M):
    c = L[i][j]
    word += c+c
  if not word == input():
    answer = "Not Eyfa"
    break
print(answer)