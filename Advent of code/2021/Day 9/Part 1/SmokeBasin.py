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

for i in range(1, len(height_map) - 1):
    for j in range(1, len(height_map[i]) - 1):
        middle = int(height_map[i][j])
        left = int(height_map[i][j - 1])
        right = int(height_map[i][j + 1])
        up = int(height_map[i - 1][j])
        down = int(height_map[i + 1][j])

        area = [left, right, up, down]
        if min(area) > middle:
            # print(int(height_map[i][j]), i, j)
            # print("up:", up)
            # print("down:", down)
            # print("left:", left)
            # print("right:", right)
            # print()
            height_sum += int(middle + 1)

print(height_sum)
