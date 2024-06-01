n = int(input())

for _ in range(n):
    nameList = []
    costList = []
    nn = int(input())
    for i in range(nn):
        a, b = input().split()
        nameList.append(b)
        costList.append(int(a))
    maxCostIndex = costList.index(max(costList))
    print(nameList[maxCostIndex])
    
        
        
    