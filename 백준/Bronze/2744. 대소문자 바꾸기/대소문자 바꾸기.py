answer = ""
for c in input():
  if c.isupper():
    answer += c.lower()
  else:
    answer += c.upper()

print(answer)