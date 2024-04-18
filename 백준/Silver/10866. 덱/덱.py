from collections import deque

N, *L = list(open(0).read().strip().split("\n"))

d = deque([])

for s in L:
  if s == "back":
    if len(d) > 0:
      print(d[-1])
    else:
      print(-1)
  elif s == "front":
    if len(d) > 0:
      print(d[0])
    else:
      print(-1)
  elif s == "empty":
    if len(d) == 0:
      print(1)
    else:
      print(0)
  elif s == "size":
     print(len(d))
  elif "pop" in s:
    if len(d) == 0:
      print(-1)
    elif "front" in s:
      print(d.popleft())
    else:
      print(d.pop())
  else:
    if "push_front" in s:
        d.appendleft(s.split(" ")[1])
    else:
        d.append(s.split(" ")[1])
    