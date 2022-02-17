ocj = list(set(input()))

ocjene = {
    1: len(ocj) == 1,
    2: len(ocj) == 2,
    3: len(ocj) == 3,
    4: len(ocj) == 4,
    5: len(ocj) == 5,
}

for k, v in ocjene.items():
    if v:
        print(k)
        break