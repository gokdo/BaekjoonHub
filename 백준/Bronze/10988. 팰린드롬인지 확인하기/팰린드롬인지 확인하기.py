s = input()

sum = ""
for c in s[len(s)-1::-1]:
    sum += c
    
if s == sum:
    print(1)
else:
    print(0)