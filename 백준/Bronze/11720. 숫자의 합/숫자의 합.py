data = list(open(0).read().split())

answer = 0

for c in data[1]:
    answer += int(c)
    
print(answer)