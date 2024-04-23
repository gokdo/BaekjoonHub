import queue
q = queue.Queue()

a,b = map(int,input().split())

for i in range(1,a+1):
    q.put(str(i))

results = []

while not q.empty():
    for i in range(b-1):
        q.put(q.get())
    results.append(q.get())
print(f"""<{", ".join(results)}>""")