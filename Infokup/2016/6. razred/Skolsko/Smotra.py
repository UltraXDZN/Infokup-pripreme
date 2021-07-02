broj_stolaca = int(input())

rjesenja = []

for i in range(1, broj_stolaca):
    for j in range(1, broj_stolaca):
        if i * j == broj_stolaca:
            rjesenja.append([min(i, j), max(i, j)])
            break

print(*rjesenja[len(rjesenja) // 2])