N = int(input())
L = [0]
i = 665

while i <10000000:
    i += 1
    if str(i).find("666") != -1:
      L.append(i)
L.sort()
print(L[N])