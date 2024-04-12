data = list(map(int,open(0).read().split()))

print(f"{min(data[1:])} {max(data[1:])}")