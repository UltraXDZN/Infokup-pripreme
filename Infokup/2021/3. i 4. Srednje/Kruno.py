def check(arr, row, col):
    return 0 <= row <= len(arr) and 0 <= col <= len(arr[0])


def neighbours(arr, row, col):
    closest = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),  # kriz
               (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]  # dijegonale
    return [(row, col) for row, col in closest if check(arr, row, col)]


def make_outline(arr):
    return [[9] * (len(arr[0]) + 1)] + [[9] + r + [9] for r in arr] + [[9] * (len(arr[0]) + 1)]


def check_pos(arr, k1, v1, k2, v2):
    ct = 0
    for x in v1:
        if arr[x[0]][x[1]] == "#":
            if arr[x[0]+1][x[1]] == "#" or arr[x[0]][x[1]+1] == "#":
                continue
            ct += 1

    if ct == 1:
        return True
    return False


def outline(arr):
    return [["X"] * (len(arr[0]) + 1)] + [["X"] + r + ["X"] for r in arr] + [["X"] * (len(arr[0]) + 1)]


r, s = map(int, input().split())
a = outline([list(input()) for i in range(r)])
pos = {}
for y in range(r):
    for x in range(s):
        if a[y][x] == "#":
            pos[x, y] = neighbours(a, y, x)

keys = list(pos.keys())
ct = 0

for i in range(0, len(keys) - 1, 2):
    ct += [0, 1][check_pos(a, keys[i], pos[keys[i]], keys[i + 1], pos[keys[i + 1]])]

print(ct)
