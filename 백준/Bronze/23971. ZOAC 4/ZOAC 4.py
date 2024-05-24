import math

H, W, N, M = map(int,input().split())


Y = H/(N+1)
X = W/(M+1)

print(math.ceil(X)*math.ceil(Y))