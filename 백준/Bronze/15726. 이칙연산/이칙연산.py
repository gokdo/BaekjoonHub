import math
A,B,C = map(int,input().split())
answer1 = A*B/C
answer2 = A/B*C
if  answer1 >= answer2:
    print(math.floor(answer1))
else:
    print(math.floor(answer2))