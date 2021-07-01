broj_bodova = int(input())

rjesenja = 0

for a in range(1, broj_bodova):
    for b in range(1, broj_bodova):
        for c in range(1, broj_bodova):
            if (a <= b <= c) and ((a + b + c) == broj_bodova):
                rjesenja += 1

print(rjesenja)