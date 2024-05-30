s = input()
dic = {}
for i in range(26):
    dic[chr(ord('a')+i)] = 0
for c in s:
  dic[c] += 1

L = []
for v in dic.values():
    L.append(v)
    
print(*L)