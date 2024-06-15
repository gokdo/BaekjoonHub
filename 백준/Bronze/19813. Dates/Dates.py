n = int(input())

for _ in range(n):
    s = input().strip()
    if s.find(".") == -1:
        m,d,y = s.strip().split("/")
    else:
        d,m,y = s.strip().split(".")

    dd = d.zfill(2)
    mm = m.zfill(2)
    yy = y.zfill(4)
    
    print(f"{dd}.{mm}.{yy} {mm}/{dd}/{yy}")