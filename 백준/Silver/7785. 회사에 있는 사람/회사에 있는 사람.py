n, *Data = list(open(0).read().split())

list = []

for i in range(int(n)):
    if Data[2*i+1] == "enter":
        list.append(Data[2*i])
    else:
        list.remove(Data[2*i])

list.sort(reverse=True)
for name in list:
    print(name)
        