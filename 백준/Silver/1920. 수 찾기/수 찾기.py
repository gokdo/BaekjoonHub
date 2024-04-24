from collections import Counter

N,NN,M,MM = open(0).read().strip().split("\n")

NL = list(map(int,NN.split()))
ML = list(map(int,MM.split()))
dic = Counter(NL)

for i in ML:
    if i in dic:
        print(1)
    else:
        print(0)