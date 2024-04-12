data = list(open(0).read().split())
for i in range(int(data[0])):
  sum = ""
  for c in data[2*i+2]: 
    sum += c * int(data[2*i+1])
  print(sum)