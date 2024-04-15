L = list(open(0).read().split())

for s in L:
  if s == "0":
    break
  else:
    if s == s[::-1]:
      print("yes")
    else:
      print("no")