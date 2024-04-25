N, *L= list(map(int,open(0).read().split()))

dic = {}
for i in range(int(N)):
  dic[i] = {'x':L[2*i], 'y':L[2*i+1]}

sorted_dic = sorted(dic, key = lambda x : (dic[x]['y'],dic[x]['x']))

for j in sorted_dic:
  print(f"{dic[j]['x']} {dic[j]['y']}")