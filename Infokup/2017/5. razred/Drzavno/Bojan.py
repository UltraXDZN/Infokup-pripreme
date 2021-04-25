n = int(input())
columns = [int(i) for i in input().split()]
k = int(input())
steps = [[int(j) for j in input().split()] for i in range(k)]
wall = [0] * n

for i in range(k):
    a, b, x = steps[i]
    part_wall = wall[a - 1:b]
    part_col = columns[a - 1:b]
    part_wall_len = len(part_wall) - part_col.count(0)
    fill = x // part_wall_len
    temp_wall = [fill if part_col[j] else 0 for j in range(len(part_wall))]
    x -= sum(temp_wall)
    j = 0 if fill % 2 == 0 else -1
    temp_wall = [a + b for a, b in zip(part_wall, temp_wall)]

    while x > 0:
        if part_col[j]:
            temp_wall[j] += 1
            x -= 1
        if j >= 0:
            j += 1
        else:
            j -= 1
    wall[a - 1:b] = temp_wall

print(*wall)
