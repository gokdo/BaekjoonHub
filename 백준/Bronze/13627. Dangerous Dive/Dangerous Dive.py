N, R = map(int,input().split())
L = list(map(int,input().split()))

answer = []
for i in range(N):
    if i+1 not in L:
        answer.append(i + 1)
answer.sort()

if N == R:
    print('*')
else:
    print(*answer)