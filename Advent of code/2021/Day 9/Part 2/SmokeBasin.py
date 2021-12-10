def check(arr, row, col):
    return 0 <= row <= len(arr) and 0 <= col <= len(arr[0])


def neighbours(arr, row, col, start):
    closest = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in closest if check(arr, row, col) and arr[row][col] == start]


def bfs(arr, row, col, val):
    start = arr[row][col]
    queue = [(row, col)]
    visited = set()
    has_changed = 0
    while queue:
        row, col = queue.pop()
        visited.add((row, col))
        arr[row][col] = val
        has_changed += 1
        # print(neighbours(arr, row, col, start))
        for row, col in neighbours(arr, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return arr


def make_outline(arr):
    return [[9] * (len(arr[0]) + 1)] + [[9] + r + [9] for r in arr] + [[9] * (len(arr[0]) + 1)]


def reset_map(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 10:
                arr[i][j] = 1
    return arr


def count_tens(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 10:
                count += 1
    return count


def check_ones(bin_arr, arr):
    for i in range(len(bin_arr)):
        for j in range(len(bin_arr[i])):
            if arr[i][j] == 10:
                bin_arr[i][j] = 1
    return bin_arr


height_map = []
while True:
    cur_input = input()
    if cur_input:
        height_map.append(cur_input)
        continue
    break

height_map = make_outline([[int(height_map[i][j]) for j in range(len(height_map[i]))] for i in range(len(height_map))])
height_sum = 0
binary_map = [[0 for j in range(len(height_map[i]))] for i in range(len(height_map))]

for i in range(len(height_map)):
    for j in range(len(height_map[i])):
        if height_map[i][j] != 9:
            height_map[i][j] = 1

basins = []
count = 0
for i in range(1, len(height_map) - 1):
    for j in range(1, len(height_map[i]) - 1):
        if binary_map[i][j] == 0 and height_map[i][j] != 9:
            height_map = bfs(height_map, i, j, 10)
            basins.append(count_tens(height_map))
            binary_map = check_ones(binary_map, height_map)
            height_map = reset_map(height_map)

basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])
