visited = []
N, r, c = map(int,input().split())

x,y = 0,0

def F(N,x,a,y,b):
  x -= a
  y -= b
  if N == 1:
    if x < 2 ** (N-1) and y < 2 ** (N-1):
      visited.append(0)
    elif x >= 2 ** (N-1) and y < 2 ** (N-1):
      visited.append(1)
    elif x < 2 ** (N-1) and y >= 2 ** (N-1):
      visited.append(2)
    else:
      visited.append(3)

  else:
    if x < 2 ** (N-1) and y < 2 ** (N-1):
      visited.append(0)
      F(N-1,x,0,y,0)
    elif x >= 2 ** (N-1) and y < 2 ** (N-1):
      visited.append(1)
      F(N-1,x,2**(N-1),y,0)
    elif x < 2 ** (N-1) and y >= 2 ** (N-1):
      visited.append(2)
      F(N-1,x,0,y,2**(N-1))
    else:
      visited.append(3)
      F(N-1,x,2 ** (N-1),y,2 ** (N-1))
      
  return visited
  
F(N,c,0,r,0)
sum = 0

for i in range(len(visited)):
  if i != len(visited)-1:
    sum += visited[i] * 4**(N-1-i)
  else: 
    sum += visited[i]
print(sum)