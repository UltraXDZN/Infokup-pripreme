def align_coords(coord):
    locations = (-1, 0, 1)
    for x in locations:
        for y in locations:
            if x == y == 0:
                continue
            yield coord[0] + x, coord[1] + y


x = 10
octopuses = "\n".join([input() for i in range(x)])

coordinates = {}
for y, line in enumerate(octopuses.split()):
    for x, val in enumerate(line):
        coordinates[(int(x), int(y))] = int(val)

flashes = 0
for _ in range(100):
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

print(flashes)
