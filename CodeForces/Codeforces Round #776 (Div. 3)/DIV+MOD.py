for _ in range(int(input())):
    l, r, a = map(int, input().split())
    e = l // a
    f = l % a

    g = r // a
    h = r % a

    print([max(g + h, g + a - 2), h + g][e == g])
