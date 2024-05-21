L = list(map(int,open(0).read().split()))

for i in range(len(L)//2):
    A,B = L[2*i],L[2*i+1]
    if A == 0 and B == 0:
        break
    elif A % B == 0:
        print("multiple")
    elif B % A == 0:
        print("factor")
    else:
        print("neither")