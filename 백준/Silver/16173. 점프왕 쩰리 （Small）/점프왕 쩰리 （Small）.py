from collections import deque

deq = deque()
dx = [1,0]
dy = [0,1]

N, *L = map(int,open(0).read().split())

Map = [[0 for _ in range(N)] for _ in range(N)]

for y in range(N):
  for x in range(N):
    Map[y][x] = L[y*N+x]

startNode = (0,0)
endNode = (N-1,N-1)

def bfs(startNode,Map):
  deq.append(startNode)
  if(Map[0][0] == 0):
    return print("Hing")

  while deq:
    curNode = deq.popleft()
    if curNode == endNode:
      return print("HaruHaru")
    
    else:
      x,y = curNode
      d = Map[y][x]
      for i in range(2):
        nx = x + dx[i]*d
        ny = y + dy[i]*d
        if 0 <= nx < N and 0 <= ny < N:
          if Map[ny][nx] != 0: 
            deq.append((nx,ny))
  return print("Hing")
bfs(startNode,Map)