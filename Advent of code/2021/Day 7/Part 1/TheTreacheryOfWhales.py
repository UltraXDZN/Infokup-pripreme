horizontal_pos = [int(x) for x in input().split(",")]

align = []
for pos in horizontal_pos:
    fuel_needed = []
    for crab in horizontal_pos:
        fuel_needed.append(abs(crab - pos))
    align.append(sum(fuel_needed))

print(min(align))