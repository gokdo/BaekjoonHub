N, *L = list(map(int,open(0).read().split()))

dic = {}
for i in range(N):
    dic[i] = {'x': L[2*i], 'y': L[2*i+1]}
    
sorted_dic = sorted(dic, key = lambda x : (dic[x]['x'],dic[x]['y']))

result = []

for ii in sorted_dic:
  result.append(f"{dic[ii]['x']} {dic[ii]['y']}")

for i in range(N):
  print(result[i])