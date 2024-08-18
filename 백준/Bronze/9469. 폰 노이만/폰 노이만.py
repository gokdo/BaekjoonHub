n = int(input())

for i in range(1, n+1):
    N, D, A, B, F = map(float,input().split())
    print(f"{N} {D/(A+B)*F}")
