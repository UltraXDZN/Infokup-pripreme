def check(arr, row, col):
    return 0 <= row <= len(arr) and 0 <= col <= len(arr[0])


def neighbours(arr, row, col, start):
    closest = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in closest if check(arr, row, col) and arr[row][col] == start]


def bfs(arr, row, col, val):
    start = arr[row][col]
    queue = [(row, col)]
    visited = set()
    while len(queue) > 0:
        row, col = queue.pop()
        visited.add((row, col))
        arr[row][col] = val
        for row, col in neighbours(arr, row, col, start):
            if (row, col) not in visited:
                visited.add((row, col))
    return arr


def make_outline(arr):
    return [[9] * (len(arr[0]) + 1)] + [[9] + r + [9] for r in arr] + [[9] * (len(arr[0]) + 1)]


height_map = []
while True:
    cur_input = input()
    if cur_input:
        height_map.append(cur_input)
        continue
    break

height_map = make_outline([[int(height_map[i][j]) for j in range(len(height_map[i]))] for i in range(len(height_map))])
height_sum = 0
for i in range(len(height_map)):
    for j in range(len(height_map[i])):
        if height_map[i][j] != 9:
            height_map[i][j] = 1

basins = []
count = 0
for i in range(1, len(height_map) - 1):
    for j in range(1, len(height_map[i]) - 1):
        if height_map[i][j] != 9:
            x = bfs(height_map, i, j, 10)
            for num in x:
                print(num)
            print(len(x))
            print()
            count += 1
        else:
            if count > 0:
                basins.append(count)
            count = 0
            continue

print(basins)
print(height_sum)
