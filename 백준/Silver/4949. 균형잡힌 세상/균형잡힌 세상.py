L = open(0).read().strip().split("\n")

for s in L:
    stack = []
    yes = True
    
    if s == ".":
        continue
   
    for c in s:
        if c == "(":
            stack.append(1)
        elif c == ")":
            if len(stack)>0 and stack[-1] == 1:
                stack.pop()
            else:
                yes = False
                break
        elif c == "[":
            stack.append(2)
        elif c == "]":
            if len(stack)>0 and stack[-1] == 2:
                stack.pop()
            else:
                yes = False
                break
        
    if yes == True and len(stack) ==0:
      print("yes")
    else:
      print("no")