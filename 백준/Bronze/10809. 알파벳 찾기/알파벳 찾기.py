s = input()
L = []

for i in range(26):
  L.append(-1)

for c in s:
  L[ord(c)-ord('a')] = s.find(c)

print(f"{L[0]} {L[1]} {L[2]} {L[3]} {L[4]} {L[5]} {L[6]} {L[7]} {L[8]} {L[9]} {L[10]} {L[11]} {L[12]} {L[13]} {L[14]} {L[15]} {L[16]} {L[17]} {L[18]} {L[19]} {L[20]} {L[21]} {L[22]} {L[23]} {L[24]} {L[25]}")