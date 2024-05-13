from collections import deque

N,M,V,*Data = list(map(int,open(0).read().split()))

def dfs(graph, start_node, visited = []):
  
  visited.append(start_node)
  
  for node in graph[start_node]:
    if node not in visited:
      dfs(graph, node, visited)
  return visited

def bfs(graph, start_node):
  
  need_visited, visited = deque(), deque()
  visited.append(start_node)
  need_visited.extend(graph[start_node])

  while need_visited:
    node = need_visited.popleft()

    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])
  return visited

graph = dict()

for i in range(1,N+1):
  graph[i] = []

for m in range(M):
  graph[Data[2*m]].append(Data[2*m+1])
  graph[Data[2*m+1]].append(Data[2*m])
    
for i in range(1,N+1):
  graph[i].sort()

print(*dfs(graph,V))
print(*bfs(graph,V))