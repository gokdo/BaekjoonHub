dic = {0: 0,1:1,2:2}
def fibonacci(n):
  if n in dic:
    return dic[n]
  else:
    dic[n] = fibonacci(n-1) + fibonacci(n-2)
    return dic[n]

T ,*L = list(map(int,open(0).read().split()))
for i in range(T):
  if L[i] == 0:
    print("1 0")
  elif L[i] == 1:
    print("0 1")
  elif L[i] == 2:
    print("1 1")
  else:
    print(f"{fibonacci(L[i]-2)} {fibonacci(L[i]-1)}")