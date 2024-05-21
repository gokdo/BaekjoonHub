T = int(input())
answer = 0
L = [0,0,0]
while 1:
    if T >= 300:
        L[0] += T // 300
        T %= 300
    elif T >= 60:
        L[1] += T // 60
        T %= 60
    elif T >= 10:
        L[2] += T // 10
        T %= 10
    elif T == 0:
        print(f"{L[0]} {L[1]} {L[2]}")
        break
    else:
        print("-1")
        break