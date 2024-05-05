import math

n, *L = list(map(int,open(0).read().split()))
L.sort()

xLine=n*0.15
if xLine - int(xLine) >= 0.5:
    xLine = math.ceil(xLine)
else:
    xLine = math.floor(xLine)
    
if n == 0:
  print(0)
else:
    result = sum(L[xLine:n-xLine])/(n-2*xLine)
    if result - int(result) >= 0.5:
        result = math.ceil(result)
    else:
        result = math.floor(result)
    print(result)
