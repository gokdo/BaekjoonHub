n = int(input())
s = ""
for i in range(n):
    s = ""
    s += i * " "
    s += 2 * ((n-1)-i) * "*" + "*"
    print(s)