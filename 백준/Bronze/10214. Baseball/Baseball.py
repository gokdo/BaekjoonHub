T = int(input())

for _ in range(T):
    scoreY, scoreK = 0, 0
    for i in range(9):
        Data = list(map(int,input().split()))
        scoreY += Data[0]
        scoreK += Data[1]
    if scoreY > scoreK:
        print("Yonsei")
    elif scoreY < scoreK:
        print("Korea")
    else:
        print("Draw")