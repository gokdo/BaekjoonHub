n = int(input())
L = list(map(int,input().split()))
a, b, c = True, False, False
answer = 0

for num in L:
    if a:
        if num == 0:
            a = False
            b = True
            answer += 1
    elif b:
        if num == 1:
            b = False
            c = True
            answer += 1
    else:
        if num == 2:
            c = False
            a = True
            answer += 1
print(answer)
        
    