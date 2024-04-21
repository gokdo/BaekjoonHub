N, *L = list(open(0).read().split())
Human = {}

for i in range(int(N)):
    a,b=int(L[2*i]),L[2*i+1]
    Human[i] = {
            'age' : a,
            'name' : b
        }

sorted_Human = sorted(Human, key = lambda x : (Human[x]['age'],x))

for order in sorted_Human:
  print(str(Human[order]['age']) +" "+ Human[order]['name'])