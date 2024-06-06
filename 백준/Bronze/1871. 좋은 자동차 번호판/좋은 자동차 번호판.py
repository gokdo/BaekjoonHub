N = int(input())

for _ in range(N):
  A,B = input().split("-")
  sumA,sumB = 0,0
  for i in range(len(A)):
    sumA += (ord(A[i])-ord('A')) * (26**(len(A)-1-i))
  sumB = int(B.lstrip("0"))
  
  if abs(sumA - sumB) <= 100:
    print("nice")
  else:
    print("not nice")