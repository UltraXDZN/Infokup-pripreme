datumi = [int(input()), int(input()), int(input()), int(input())]
tren_datum = int(input())

stanje_mjeseca = {
    "MLADI": datumi[0],
    "PRVA": datumi[1],
    "PUNI": datumi[2],
    "ZADNJA": datumi[3]
}

for k in stanje_mjeseca.keys():
    for k2 in stanje_mjeseca.keys():
        if stanje_mjeseca[k] < tren_datum <= stanje_mjeseca[k2]:
            print(k)
        elif stanje_mjeseca[k] >= tren_datum > stanje_mjeseca[k2]:
            print(k2)