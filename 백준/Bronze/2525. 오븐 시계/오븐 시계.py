H,M,overTime = map(int,open(0).read().split())

M=M+overTime

while M >= 60:
  M -= 60
  H += 1
 
while H >= 24:
  H -= 24
print(f"{H} {M}")