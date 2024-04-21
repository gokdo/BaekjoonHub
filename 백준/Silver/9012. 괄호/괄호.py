T, *L = list(open(0).read().split())

stack = []

for i in range(int(T)):
    for ii in L[i]:
        if ii == "(":
            stack.append(1)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                stack.append(1)
                break
                
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
        stack.clear()