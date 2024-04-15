N, *L = list(map(int,open(0).read().split()))

answer = 0
count = 0

for i in L:
  for n in range(1,i+1):
    if i % n == 0:
        count += 1
  if count == 2:
    answer += 1
  count = 0

print(answer)