horizontal_pos = [int(x) for x in input().split(",")]


def calc_sum(num):
    rnum = 0
    for i in range(num):
        rnum += i + 1
    return rnum


align = []
for pos in horizontal_pos:
    fuel_needed = []
    for crab in horizontal_pos:
        fuel_needed.append(calc_sum(abs(crab - pos)))
        print(crab, pos, calc_sum(abs(crab - pos)))
    print(sum(fuel_needed))
    print()
    align.append(sum(fuel_needed))

print(min(align))
