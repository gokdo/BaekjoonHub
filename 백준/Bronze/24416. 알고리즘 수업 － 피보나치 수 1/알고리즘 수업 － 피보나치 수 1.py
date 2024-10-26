global countA
global countB

f = [0] * 42
n = int(input())

countA = 0
countB = 0

def fib(n):
    global countA
    if n == 1 or n == 2:
      countA += 1
      return 1
    else:
      return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    global countB
    f[1], f[2] = 1, 1
    for i in range(3,n+1):
        countB += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

fib(n)
fibonacci(n)
print(f"{countA} {countB}")