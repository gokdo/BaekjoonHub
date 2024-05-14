N, *Data = list(open(0).read().split())
N = int(N)
L = len(Data[0])
falseList = [True for _ in range(L)] 
for s in range(1,N):
    for c in range(L):
               if Data[s][c] != Data[0][c]:
                   falseList[c] = False
answer = ""
for i in range(L):
  if falseList[i] == False:
    answer += '?'
  else:
    answer += Data[0][i]
print(answer)
