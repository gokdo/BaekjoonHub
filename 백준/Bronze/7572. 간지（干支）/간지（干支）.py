gan = ["0","1","2","3","4","5","6","7","8","9"]
ji = ["A","B","C","D","E","F","G","H","I","J","K","L"]
g = 6
j = 8
i = 0
n = int(input())
if n-4 >= 60:
  n = (n-4)%60 + 4
while i < n:
   i += 1
   if g < 9:
    g += 1
   else:
    g = 0
   if j < 11:
    j += 1
   else:
    j = 0
print(ji[j] + gan[g])