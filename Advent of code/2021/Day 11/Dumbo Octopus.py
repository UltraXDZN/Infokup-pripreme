def make_outline(arr):
    return [[-1] * (len(arr[0]) + 1)] + [[-1] + r + [-1] for r in arr] + [[-1] * (len(arr[0]) + 1)]


def print_list(arr):
    for row in arr:
        print(*row)


x = 10
octopuses = [list(map(int, list(input()))) for i in range(x)]
no_increase = [10, 0, -1]

#
# def get_neighbours(x, y):
#     return filter(lambda octopus: octopus in octopuses,
#                   [(x - 1, y),
#                    (x - 1, y - 1),
#                    (x, y - 1),
#                    (x + 1, y - 1),
#                    (x + 1, y),
#                    (x + 1, y + 1),
#                    (x, y + 1),
#                    (x - 1, y + 1)
#                    ])
#
#
# print(0 + get_neighbours(0, 0))

# for i in range(x):
flashes = 0
# for _ in range(10):
for i in range(1, x):
    for j in range(1, x):
        if octopuses[i][j] + 1 >= 10 or octopuses[i][j] >= 10:
            octopuses[i][j] = 0

            flashes += sum([
                [0, 1][octopuses[i - 1][j] not in no_increase],
                [0, 1][octopuses[i - 1][j + 1] not in no_increase],
                [0, 1][octopuses[i - 1][j - 1] not in no_increase],

                [0, 1][octopuses[i][j + 1] not in no_increase],
                [0, 1][octopuses[i][j - 1] not in no_increase],

                [0, 1][octopuses[i + 1][j] not in no_increase],
                [0, 1][octopuses[i + 1][j + 1] not in no_increase],
                [0, 1][octopuses[i + 1][j - 1] not in no_increase]
            ])

            octopuses[i - 1][j] += [0, 1][octopuses[i - 1][j] not in no_increase]
            octopuses[i - 1][j + 1] += [0, 1][octopuses[i - 1][j + 1] not in no_increase]
            octopuses[i - 1][j - 1] += [0, 1][octopuses[i - 1][j - 1] not in no_increase]

            octopuses[i][j + 1] += [0, 1][octopuses[i][j + 1] not in no_increase]
            octopuses[i][j - 1] += [0, 1][octopuses[i][j - 1] not in no_increase]

            octopuses[i + 1][j] += [0, 1][octopuses[i + 1][j] not in no_increase]
            octopuses[i + 1][j + 1] += [0, 1][octopuses[i + 1][j + 1] not in no_increase]
            octopuses[i + 1][j - 1] += [0, 1][octopuses[i + 1][j - 1] not in no_increase]

        else:
            octopuses[i][j] += [0, 1][octopuses[i][j] not in no_increase]

        print_list(octopuses[:i])
        # print()
        # print(octopuses[i])
        # print()
        # print()

print_list(octopuses)
print(flashes)
print()
