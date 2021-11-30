n, m = map(int, input().split())

lr = True
a = ["."] * m
for i in range(n):
    if i % 2 != 0:
        a[[0, -1][lr]] = "#"
        print("".join(a))
        a[[0, -1][lr]] = "."
        lr = not lr
        continue
    print("#" * m)
