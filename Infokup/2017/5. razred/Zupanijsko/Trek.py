pocetni_broj = int(input())
zavrsni_broj = int(input())

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

brojac_prvi = []
brojac_drugi = []
for i in range(len(edgeovi)):
    if (edgeovi[pocetni_broj][i] != 0):
        brojac_prvi.append(edgeovi[pocetni_broj][i])


for i in range(len(edgeovi)):
    if(edgeovi[zavrsni_broj-1][i] != 0):
        brojac_drugi.append(edgeovi[zavrsni_broj-1][i])

# res = []
# for i in range(14):
#     if brojac[i] != 0:
#         res.append(brojac[i])
print(brojac_prvi[1] + brojac_drugi[1])
