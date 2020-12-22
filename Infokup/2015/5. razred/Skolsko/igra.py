bodovi = []
for i in range(4):
    bodovi_na_razini = int(input())
    bodovi.append((bodovi_na_razini))

brojac = 0
for i in range(4):
    brojac += bodovi[i]
    print(brojac)

if brojac > 100:
    print("DA")
else:
    print("NE")
