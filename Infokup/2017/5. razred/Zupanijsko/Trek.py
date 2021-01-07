pocetni_broj = int(input())
zavrsni_broj = int(input())


def pronadji_najkraci_put(pocetni_broj, zavrsni_broj, graf):
    posjeceni_brojevi = [pocetni_broj]
    duljina_puta = []
    for i in range(14):
        if graf[pocetni_broj][i] != 0:
            rekuzrzivna_duljina = pronadji_put(i, zavrsni_broj, graf, posjeceni_brojevi, graf[pocetni_broj][i])
            if rekuzrzivna_duljina != -1:
                duljina_puta.append(rekuzrzivna_duljina)

    if len(duljina_puta) == 0:
        return -1
    return min(duljina_puta)

def pronadji_put(trenutni_broj, zavrsni_broj, posjeceni_brojevi, graf, pozicija_na_grafu):
    if trenutni_broj == zavrsni_broj:
        return pozicija_na_grafu

    rekurzivne_duljine = []
    posjeceni_brojevi.append(trenutni_broj)
    for i in range(14):
        if graf[trenutni_broj][i] != 0:
            if i not in posjeceni_brojevi:
                rekuzrzivna_duljina = pronadji_put(i, zavrsni_broj, graf, posjeceni_brojevi, graf[trenutni_broj][i] + pozicija_na_grafu)
                rekurzivne_duljine.append(rekuzrzivna_duljina)
    if len(rekurzivne_duljine) == 0:
        return -1
    return min(rekurzivne_duljine)


edgeovi = []
for i in range(14):
    row = []
    for j in range(14):
        row.append(0)
    edgeovi.append(row)

# print(len(edgeovi))
for i in range(7):
    edgeovi[i][i+7] = 20
    edgeovi[i+7][i] = 20

for i in range(7):
    edgeovi[i % 7][(i+1) % 7] = 10
    edgeovi[(i+1) % 7][i % 7] = 10

for i in range(7):
    edgeovi[i % 7 + 7][(i+1) % 7 + 7] = 30
    edgeovi[(i+1) % 7 + 7][i % 7 + 7] = 30

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in edgeovi]))

print(pronadji_najkraci_put(pocetni_broj, zavrsni_broj, edgeovi))
# brojac_prvi = []
# brojac_drugi = []
# for i in range(len(edgeovi)):
#     if (edgeovi[pocetni_broj][i] != 0):
#         brojac_prvi.append(edgeovi[pocetni_broj][i])
#
#
# for i in range(len(edgeovi)):
#     if(edgeovi[zavrsni_broj-1][i] != 0):
#         brojac_drugi.append(edgeovi[zavrsni_broj-1][i])
#
# print(brojac_prvi, brojac_drugi)
