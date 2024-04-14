import math

T, *L = list(map(int,open(0).read().split()))

front = 0; middle = ""; last = 0;
for i in range(T):
  H = L[3*i]
  W = L[3*i+1]
  N = L[3*i+2]

  if N % H == 0:
    front = H
  else:
    front = N%H

  last = math.ceil(N/H)

  if last < 10:
    middle = "0"
  else:
    middle = ""

  print(f"{front}"+f"{middle}"+f"{last}")