l = int(input())
s = input()
sum = 0

for i in range(len(s)):
  sum += (ord(s[i])-ord('a')+1) * (31**i)

print(sum % 1234567891)