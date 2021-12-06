from collections import Counter


def find_fish(fishes, loop_n):
    for i in range(loop_n):
        fishes = {n: fishes[n + 1] for n in range(-1, 8)}
        fishes[8] = fishes[-1]
        fishes[6] += fishes[-1]
        fishes[-1] = 0
    return fishes


lanternfish = Counter([int(x) for x in input().split(",")])

print(sum(find_fish(lanternfish, 80).values()))
print(sum(find_fish(lanternfish, 156).values()))
