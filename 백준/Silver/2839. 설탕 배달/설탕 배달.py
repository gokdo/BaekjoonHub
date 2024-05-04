N = int(input())
cant = [4,7]
answer = 0
if N in cant:
    answer = -1
else:
    for x in range(1001,-1,-1):
        for y in range(0,10):
            if 5*x + 3*y == N:
                answer = x+y
                break
            if answer != 0:
              break
print(answer)

        