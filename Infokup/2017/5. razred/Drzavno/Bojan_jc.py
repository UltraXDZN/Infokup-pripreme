# n = 6
# columns = [1, 1, 1, 1, 1, 1]
# k = 4
# steps = [
#     [1, 3, 5],
#     [2, 4, 6],
#     [3, 6, 2],
#     [1, 6, 11],
# ]
# n = 9
# columns = [1, 0, 1, 1, 1, 0, 1, 1, 0]
# k = 3
# steps = [
#     [1, 5, 7],
#     [7, 8, 4],
#     [1, 2, 3],
# ]

# n = 8
# columns = [1, 0, 1, 0, 1, 0, 1, 0]
# k = 2
# steps = [
#     [1, 6, 10],
#     [3, 6, 11],
# ]

n = 7
columns = [1, 1, 1, 1, 1, 1, 1]
k = 3
steps = [
    [1, 5, 500000000],
    [3, 7, 600000000],
    [1, 7, 900000000],
]

wall = [0] * n

for i in range(k):
    a, b, x = steps[i]
    temp_wall = wall[a - 1:b]
    j = 0
    left_right = True
    while x > 0:
        if columns[a-1+j] == 1:
            temp_wall[j] += 1
            x -= 1
        if left_right and j < len(temp_wall) - 1:
            j += 1
        elif left_right and j == len(temp_wall) - 1:
            left_right = False
        elif not left_right and j > 0:
            j -= 1
        elif not left_right and j == 0:
            left_right = True
    wall[a - 1:b] = temp_wall
    print(f"Korak - {i+1}. gotov")

print(*wall)
