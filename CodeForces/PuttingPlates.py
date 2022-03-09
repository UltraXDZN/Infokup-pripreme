def verify(coord):
    return [False, True][0 <= coord[0] < w and 0 <= coord[1] < h and coord not in cant_put]


def neighbours(x, y):
    positions = [(x, y + 1),
                 (x, y - 1),
                 (x + 1, y),
                 (x - 1, y),
                 (x + 1, y + 1),
                 (x - 1, y + 1),
                 (x + 1, y - 1),
                 (x - 1, y - 1)]
    return [position for position in positions if verify(position)]


for _ in range(int(input())):
    cant_put = []
    h, w = map(int, input().split())
    a = [[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if (j, i) not in cant_put and (i in [0, h-1] or j in [0, w-1]):
                cant_put += neighbours(j, i)
                a[i][j] = 1

    for i in range(h):
        print(*a[i], sep="")
    print()
