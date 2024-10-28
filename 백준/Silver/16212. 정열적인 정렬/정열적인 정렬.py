N, *L = list(map(int,open(0).read().split()))
L.sort()

answer = ""
for l in L:
  answer += str(l) + " " 
print(answer.rstrip())