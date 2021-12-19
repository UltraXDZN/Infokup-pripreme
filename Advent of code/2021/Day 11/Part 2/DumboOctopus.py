def align_coords(coord):
    locations = (-1, 0, 1)
    for x in locations:
        for y in locations:
            if x == y == 0:
                continue
            yield coord[0] + x, coord[1] + y


def check_all_zero(dict_v):
    n_of_zeros = 0
    for num in dict_v:
        if num == 0:
            n_of_zeros += 1
    return n_of_zeros == len(dict_v)


x = 10
octopuses = "\n".join([input() for i in range(x)])

coordinates = {}
for y, line in enumerate(octopuses.split()):
    for x, val in enumerate(line):
        coordinates[(int(x), int(y))] = int(val)

flashes = 0
step = 1
while True:
    flash = []
    for k, v in coordinates.items():
        coordinates[k] += 1
        if coordinates[k] == 10:
            flash.append(k)

    while flash:
        part = flash.pop()
        if coordinates[part] == 0:
            continue
        coordinates[part] = 0
        flashes += 1

        for other_coord in align_coords(part):
            if other_coord in coordinates and coordinates[other_coord] != 0:
                coordinates[other_coord] += 1
                if coordinates[other_coord] == 10:
                    flash.append(other_coord)

    if check_all_zero(coordinates.values()):
        break
    step += 1

print(step)
