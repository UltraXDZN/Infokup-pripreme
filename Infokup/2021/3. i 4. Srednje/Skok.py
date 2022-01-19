def check_valid_pos(x, y):
    return [False, True][0 <= y < len(ploca) and 0 <= x < len(ploca[y])]


def neighbours(row, col):
    closest = [(row - 2, col - 1), (row + 2, col - 1), (row - 1, col - 2), (row + 1, col - 2),
               (row - 2, col + 1), (row + 2, col + 1), (row - 1, col + 2), (row + 1, col + 2)]
    return [(row, col) for row, col in closest if check_valid_pos(col, row)]


def reset_dict():
    for y in range(r):
        for x in range(s):
            bomboni[y, x] = ploca[y][x]


def find_next_branch(x, y, s):
    coords = neighbours(x, y)
    for coord in coords:
        if bomboni[x, y] > 0 and bomboni[coord] > 0:
            s += bomboni[x, y]
            bomboni[x, y] = 0
            s = find_next_branch(coord[0], coord[1], s)
            break
    return s + bomboni[x, y]


r, s = map(int, input().split())
ploca = [[int(x) for x in input().split()] for i in range(r)]
bomboni = {}
reset_dict()
positions = []
bomboni_s = bomboni.copy()
for k, v in bomboni_s.items():
    reset_dict()
    solution = find_next_branch(k[0], k[1], 0)
    positions.append(solution)

print(max(positions))
