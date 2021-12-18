a = input() + input()
a, b = (ord(a[i]) - ord(a[i + 2]) for i in (0, 1))
print(max(a, -a, b, -b))
i = 10
while a != 0 or b != 0:
    r = ["", "R"][a < 0]
    a += [0, 1][a < 0]

    r = [r, "L"][a > 0]
    a -= [0, 1][a > 0]

    r += ["", "U"][b < 0]
    b += [0, 1][b < 0]

    r += ["", "D"][b > 0]
    b -= [0, 1][b > 0]
    print(r)
