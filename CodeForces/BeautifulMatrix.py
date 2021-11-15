matrix = [[int(x) for x in input().split()] for i in range(5)]

for i in range(5):
    for j in range(5):
        x, y = i, j
        if matrix[x][y] == 1:
            if i > 2:
                x = 4 - x
            if j < 2:
                y = 4 - y
            if x == y == 2:
                print(0)
            elif x == y:
                print(x - (x % 2))
            else:
                print(max(x, y) - min(x, y))

