datumi = [int(input()), int(input()), int(input()), int(input())]
tren_datum = int(input())

stanje_mjeseca = {
    "MLADI": datumi[0],
    "PRVA": datumi[1],
    "PUNI": datumi[2],
    "ZADNJA": datumi[3]
}

datumi_stanja = list(stanje_mjeseca.values())
nazivi_stanja = list(stanje_mjeseca.keys())

for i in range(len(datumi_stanja)):
    if tren_datum < datumi_stanja[i]:
        print(nazivi_stanja[i - 1])
        print(datumi_stanja[i] - tren_datum)
        break

    elif tren_datum == datumi_stanja[i]:
        print(nazivi_stanja[i])
        if tren_datum >= datumi_stanja[-1]:
            print(31 - tren_datum)
            break
        print(datumi_stanja[i + 1] - tren_datum)
        break

