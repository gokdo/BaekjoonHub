m = int(input())
n = int(input())
point = 0

for i in range(m, n+1):
  s = str(i)
  if len(s) % 2 == 1:
    if s[len(s) // 2] == "0" or s[len(s) // 2] == "1" or s[len(s) // 2] == "8":
      if len(s) == 1:
        point += 1
        continue
      for i in range(len(s)//2):
        if s[i] == "2" or s[i] == "3" or s[i] == "4" or s[i] == "5" or s[i] == "7":
          point -= 1
          break
        if s[i] == "0" or s[i] == "1" or s[i] == "8":
          if s[i] == s[len(s)-1-i]:
            pass
          else:
            point -= 1
            break
        if s[i] == "6":
          if s[len(s)-1-i] == "9":
            pass
          else:
            point -= 1
            break
        if s[i] == "9":
          if s[len(s)-1-i] == "6":
            pass
          else:
            point -= 1
            break
      point += 1
    else:
      continue
  else:
      for i in range(len(s)//2):
        if s[i] == "2" or s[i] == "3" or s[i] == "4" or s[i] == "5" or s[i] == "7":
            point -= 1
            break
        if s[i] == "0" or s[i] == "1" or s[i] == "8":
          if s[i] == s[len(s)-1-i]:
            pass
          else:
            point -= 1
            break
        if s[i] == "6":
          if s[len(s)-1-i] == "9":
            pass
          else:
            point -= 1
            break
        if s[i] == "9":
          if s[len(s)-1-i] == "6":
            pass
          else:
            point -= 1
            break
      point += 1

print(point)