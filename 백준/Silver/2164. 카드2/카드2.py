from queue import Queue

N = int(input())
q = Queue()
for i in range(1,N+1):
    q.put(i)
size = N
for i in range(N):
    while(size>1):
        q.get()
        p = q.get()
        q.put(p)
        size -=1
print(q.get())