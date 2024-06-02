i = int(input())

dp = {}
dp[i] = 0

while i > 1:
  if i in dp:
    if i % 3 == 0:
      nexti = i // 3
      if nexti in dp:
        if dp[nexti] > dp[i] + 1:
          dp[nexti] = dp[i] + 1
      else:
        dp[nexti] = dp[i] + 1
    if i % 2 == 0:
      nexti = i // 2
      if nexti in dp:
        if dp[nexti] > dp[i] + 1:
          dp[nexti] = dp[i] + 1
      else:
        dp[nexti] = dp[i] + 1
    nexti = i - 1
    if nexti in dp:
      if dp[nexti] > dp[i] + 1:
        dp[nexti] = dp[i] + 1
    else:
      dp[nexti] = dp[i] + 1
  i-=1
print(dp[1])
