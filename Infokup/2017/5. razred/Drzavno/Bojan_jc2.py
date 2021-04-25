# PR. 1
# n = 6
# columns = [1, 1, 1, 1, 1, 1]
# k = 4
# steps = [
#     [1, 3, 5],
#     [2, 4, 6],
#     [3, 6, 2],
#     [1, 6, 11],
# ]

# PR. 2
# n = 9
# columns = [1, 0, 1, 1, 1, 0, 1, 1, 0]
# k = 3
# steps = [
#     [1, 5, 7],
#     [7, 8, 4],
#     [1, 2, 3],
# ]

# PR. 3
# n = 7
# columns = [1, 1, 1, 1, 1, 1, 1]
# k = 3
# steps = [
#     [1, 5, 500000000],
#     [3, 7, 600000000],
#     [1, 7, 900000000],
# ]

# PR. 4
n = 8
columns = [1, 0, 1, 0, 1, 0, 1, 0]
k = 2
steps = [
    [1, 6, 10],
    [3, 6, 11],
]

wall = [0] * n

for i in range(k):
    a, b, x = steps[i]
    part_wall = wall[a - 1:b]
    part_col = columns[a - 1:b]
    part_wall_len = len(part_wall) - part_col.count(0)
    temp_wall = [x // part_wall_len if part_col[j] == 1 else 0 for j in range(len(part_wall))]
    x -= sum(temp_wall)
    j = 0 if temp_wall[0] % 2 == 0 else -1
    temp_wall = [a + b for a, b in zip(part_wall, temp_wall)]

    while x > 0:
        if part_col[j] == 1:
            temp_wall[j] += 1
            x -= 1
        if j >= 0:
            j += 1
        else:
            j -= 1
    wall[a - 1:b] = temp_wall

print(*wall)
