N, *L = list(open(0).read().strip().split("\n"))

q = []

for s in L:
  if s == "back":
    if len(q) > 0:
      print(q[-1])
    else:
      print(-1)
  elif s == "front":
    if len(q) > 0:
      print(q[0])
    else:
      print(-1)
  elif s == "empty":
    if len(q) == 0:
      print(1)
    else:
      print(0)
  elif s == "size":
     print(len(q))
  elif s == "pop":
    if len(q) == 0:
      print(-1)
    else:
      print(q.pop(0))
  else:
    q.append(s.split(" ")[1])