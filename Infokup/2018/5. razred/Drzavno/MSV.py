broj_bacanja_kocke = int(input())

ukupni_bomboni = {
    0: [],
    1: [],
    2: []
}

brojac = 0
trenutni_brojac = 0
novi_broj = 0
while brojac < broj_bacanja_kocke:
    if novi_broj != 6:
        trenutni_brojac = 0 if brojac % 3 == 0 else trenutni_brojac
    else:
        brojac -= 1
        trenutni_brojac -= 1
        broj_bacanja_kocke -= 1

    novi_broj = int(input())
    ukupni_bomboni[trenutni_brojac].append(novi_broj)
    # print(ukupni_bomboni[trenutni_brojac], trenutni_brojac, brojac)

    trenutni_brojac += 1
    brojac += 1

print(sum(ukupni_bomboni[0]) + sum(ukupni_bomboni[1]) + sum(ukupni_bomboni[2]))
print(sum(ukupni_bomboni[0]), sum(ukupni_bomboni[1]), sum(ukupni_bomboni[2]))
