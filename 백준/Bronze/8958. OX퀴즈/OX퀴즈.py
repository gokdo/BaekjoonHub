L = list(open(0).read().split())

for i in range(int(L[0])):
  s = L[i+1]
  score = 0
  sum = 0
  for c in s:
    if c == 'O':
      score += 1
      sum += score
    else:
      score = 0
  print(sum)