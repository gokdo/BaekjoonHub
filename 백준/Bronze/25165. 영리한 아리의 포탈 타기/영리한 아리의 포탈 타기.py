y, x = map(int,input().split())
Ax, D = map(int,input().split())
Sy, Sx = map(int,input().split())
answer = "NO..."

if y % 2 == 0:
    if D == 0:
        pass
    elif D == 1:
        if Sy == y:
            answer = "YES!"
        else:
            pass
elif y % 2 == 1:
    if D == 0:
        if Sy == y:
            answer = "YES!"
        else:
            pass
    elif D == 1:
        pass
print(answer)