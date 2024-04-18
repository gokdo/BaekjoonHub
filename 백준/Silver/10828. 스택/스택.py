N,*L = list(open(0).read().strip().split("\n"))

stack = []

for s in L:
  if s == "top":
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
  elif s == "empty":
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif s == "size":
     print(len(stack))
  elif s == "pop":
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  else:
    stack.append(s.split(" ")[1])
    
 