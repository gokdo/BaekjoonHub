T, N, *L = list(open(0).read().split())
T = int(T)
N = int(N)
sum = 0
def weekCalc(someday,time):
  if someday == "Mon":
    return 0 + int(time)
  elif someday == "Tue":
    return 24 + int(time)
  elif someday == "Wed":
    return 48 + int(time)
  elif someday == "Thu":
    return 72 + int(time)
  elif someday == "Fri":
    return 96 + int(time)

for i in range(N):
  sum += weekCalc(L[4*i+2],L[4*i+3]) - weekCalc(L[4*i],L[4*i+1])

if sum >= T:
  print(0)
else:
  if T-sum > 48:
    print(-1)
  else:
    print(T-sum)