A,B,V = map(int,input().split())

C=A-B
if (V-A)% C==0:
  day = (V-A)//C + 1
else:
  day = (V-A)//C + 2
print(day)