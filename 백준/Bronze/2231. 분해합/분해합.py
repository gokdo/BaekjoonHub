N = int(input())

answer = 0
for x in range(N+1):
  if x + sum(map(int,f"{x}")) == N:
    answer = x
    break
print(answer)