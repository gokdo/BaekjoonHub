N, *L, v= list(map(int, open(0).read().split()))

answer = 0

for i in L:
  if i == v:
    answer += 1

print(answer)