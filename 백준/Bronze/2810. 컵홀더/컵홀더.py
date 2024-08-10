n = int(input())
s = input()

sum = 1
i = 0
while i < n:
  if s[i] == "S":
    i += 1
    sum += 1
  elif s[i] =="L":
    i += 2
    sum += 1

if sum > n:
  sum = n
print(sum)