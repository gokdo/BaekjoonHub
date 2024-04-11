import sys

answer = []

data = list(map(int,open(0).read().split()))

for i in range(1,31):
  a = data.count(i)
  if a == 0:
    answer.append(i)
print(f"{min(answer)}\n{max(answer)}")