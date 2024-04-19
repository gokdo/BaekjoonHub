import math

N = math.factorial(int(input()))

s = str(N)[::-1]
answer = 0

for c in s:
    if c == "0":
        answer += 1
    else:
        break
        
print(answer)
