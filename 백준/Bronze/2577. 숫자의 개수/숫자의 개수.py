L = list(map(int,open(0).read().split()))
sum = 1

for l in L:
  sum *= l

s = f"{sum}"
print(f"{s.count('0')}\n{s.count('1')}\n{s.count('2')}\n{s.count('3')}\n{s.count('4')}\n{s.count('5')}\n{s.count('6')}\n{s.count('7')}\n{s.count('8')}\n{s.count('9')}")
