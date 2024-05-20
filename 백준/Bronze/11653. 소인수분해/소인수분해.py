N = int(input())
n = 2
while N > 1:
    if N % n == 0:
        print(n)
        N /= n
    else:
        n += 1