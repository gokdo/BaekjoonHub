L = list(map(int, open(0).read().split()))

m = max(L)
i = L.index(m)+1
print(f"{m}\n{i}")