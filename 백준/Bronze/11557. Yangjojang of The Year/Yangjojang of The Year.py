T = int(input())
for _ in range(T):
  N = int(input())
  name = []
  amount = []
  for i in range(N):
    a,b = input().split()
    name.append(a)
    amount.append(int(b))
  print(name[amount.index(max(amount))])