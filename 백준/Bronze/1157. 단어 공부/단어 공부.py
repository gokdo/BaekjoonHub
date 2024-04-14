s = input().upper()

L = []

for i in range(26):
  L.append(0)

for c in s:
  L[ord(c) - ord('A')] += 1

if L.count(max(L)) == 1:
  print(f"{chr(L.index(max(L))+ord('A'))}")
else:
  print("?")