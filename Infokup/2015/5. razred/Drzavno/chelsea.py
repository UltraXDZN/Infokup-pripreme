br_utakmica = int(input())
golovi_uk = []
golovi_drugo_pol = []
golovi_prvo_pol = []


def broj_bodova(lista, n):
    br_bodova = 0
    for i in range(n):
        for j in range(0, 2, 2):
            if lista[i][j] > lista[i][j + 1]:
                br_bodova += 3
            elif lista[i][j] == lista[i][j + 1]:
                br_bodova += 1
    return br_bodova


for i in range(br_utakmica):
    golovi_na_utakmici = [int(i) for i in input().split()]
    golovi_uk.append((golovi_na_utakmici[0], golovi_na_utakmici[1]))
    golovi_prvo_pol.append((golovi_na_utakmici[2], golovi_na_utakmici[3]))
for i in range(br_utakmica):
    for j in range(0, 2, 2):
        golovi_drugo_pol.append(
            (golovi_uk[i][j] - golovi_prvo_pol[i][j], golovi_uk[i][j + 1] - golovi_prvo_pol[i][j + 1]))
print(broj_bodova(golovi_uk, br_utakmica))
print(broj_bodova(golovi_prvo_pol, br_utakmica))
print(broj_bodova(golovi_drugo_pol, br_utakmica))
