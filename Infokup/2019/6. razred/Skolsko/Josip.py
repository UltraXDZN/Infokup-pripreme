broj_natjecatelja = int(input())
oznaka_josipa = int(input()) - 1

bodovi = []
brojac_vecih = 0

for i in range(broj_natjecatelja):
    bodovi.append(int(input()))

for i in range(broj_natjecatelja):
    if bodovi[oznaka_josipa] < bodovi[i]:
        brojac_vecih += 1

print(brojac_vecih)
