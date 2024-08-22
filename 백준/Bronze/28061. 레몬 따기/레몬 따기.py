n = int(input())
L = list(map(int,input().split()))

answer = 1
for i in range(n):
    answer -= 1
    if L[i] > answer:
        answer = L[i]
print(answer - 1)