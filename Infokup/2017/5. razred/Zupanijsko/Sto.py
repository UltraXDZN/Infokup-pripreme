broj_brojeva = int(input())
brojevi = []

for i in range(broj_brojeva):
    brojevi.append(int(input()))

zbrajac = 0
for broj in brojevi:
    zbrajac += broj
    if zbrajac == 100:
        print(broj)
        break
    if zbrajac > 100:
        zbrajac = broj
        print(broj)
        continue
    if zbrajac + broj <= 100:
        print(broj)
        continue
