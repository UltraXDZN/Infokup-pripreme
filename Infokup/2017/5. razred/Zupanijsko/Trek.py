pocetni_broj = int(input())
zavrsni_broj = int(input())


def pronadji_najkraci_put(start, end, graph):
    posjeceni_brojevi = [start]
    putevi = []

    for i in range(14):
        if graph[start][i] != 0:
            put = pronadji_put(i, end, graph, posjeceni_brojevi, graph[start][i])
            if put != -1:
                putevi.append(put)

    if len(putevi) == 0:
        return -1
    else:
        return min(putevi)


def pronadji_put(trenutni_broj, krajnji_broj, graf, posjeceni_brojevi, pozicija_na_grafu):
    if trenutni_broj == krajnji_broj:
        return pozicija_na_grafu

    duljine = []
    posjeceni_brojevi.append(trenutni_broj)
    for i in range(14):
        if graf[trenutni_broj][i] != 0:
            if i not in posjeceni_brojevi:
                put = pronadji_put(i, krajnji_broj, graf, posjeceni_brojevi, pozicija_na_grafu + graf[trenutni_broj][i])
                if put != -1:
                    duljine.append(put)

    if len(duljine) == 0:
        return -1
    else:
        return min(duljine)

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

#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in edgeovi]))

print(pronadji_najkraci_put(pocetni_broj-1, zavrsni_broj-1, edgeovi))
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
