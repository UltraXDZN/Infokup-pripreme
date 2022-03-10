def search_wall(x, y, a):
    for i in range(max_y - y + 1):
        for j in range(max_x - x + 1):
            if "." == a[i][j] == a[i][j + x - 1] == a[i + y - 1][j] == a[i + y - 1][j + x - 1]\
                    and a[i][j:j + x].count(".") == x and a[i+y // 2][j] == ".":
                return j, i
    return 0, 0


def print_list(a):
    for i in range(len(a)):
        print(*a[i], sep="")


max_y, max_x, t = map(int, input().split())
tablica = [['.' for j in range(max_x)] for i in range(max_y)]
increment_x, increment_y = 0, 0
temp_y = 0
for _ in range(t):
    y, x = map(int, input().split())
    increment_x, increment_y = search_wall(x, y, tablica)
    tablica[increment_y] = tablica[increment_y][:increment_x] + \
                           ["+"] + (["-"] * (x - 2)) + ["+"] + \
                           tablica[increment_y][(x + increment_x):]

    for i in range(increment_y, increment_y + y - 2):
        tablica[i + 1] = \
            tablica[i + 1][:increment_x] + \
            ["|"] + (["#"] * (x - 2)) + ["|"] + \
            tablica[i + 1][(x + increment_x):]

    tablica[increment_y + y - 1] = tablica[increment_y + y - 1][:increment_x] + \
                                   ["+"] + (["-"] * (x - 2)) + ["+"] + \
                                   tablica[increment_y + y - 1][x + increment_x:]

print_list(tablica)
