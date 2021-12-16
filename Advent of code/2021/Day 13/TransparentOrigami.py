def print_list(arr):
    for row in arr:
        print(*row, sep="")


points = set()
while True:
    try:
        x, y = map(int, input().split(","))
        points.add((int(x), int(y)))
    except ValueError:
        break

has_printed_p1 = False
while True:

    fold = input()
    if "x=" in fold:

        fold = int(fold.replace("fold along x=", ""))
        points = {([fold - (x - fold), x][x < fold], y) for x, y in points}
    elif "y=" in fold:

        fold = int(fold.replace("fold along y=", ""))
        points = {(x, [fold - (y - fold), y][y < fold]) for x, y in points}
    else:
        break
    if not has_printed_p1:
        print(f"Part 1: {len(points)}")
        has_printed_p1 = True

x_s, y_s = zip(*points)

table = [[" " for j in range(max(x_s) + 1)] for i in range(max(y_s) + 1)]

for i in range(len(x_s)):
    for y in range(y_s[i] + 1):
        for x in range(x_s[i] + 1):
            if y == y_s[i] and x == x_s[i]:
                table[y][x] = "#"


print()
print("Part 2:")
print_list(table)