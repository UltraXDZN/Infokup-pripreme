pocetak = int(input())
zavrsni_kvadrat = int(input())
korak = int(input())
broj_lokvi = int(input())

lokve = []

for i in range(broj_lokvi):
    lokve.append(int(input()))

br_stanutih_lokvi = 1

for i in range(pocetak, zavrsni_kvadrat+1, korak):
    if i in lokve:
        br_stanutih_lokvi += 1

print(br_stanutih_lokvi-1)


potenc_korak = 1
while br_stanutih_lokvi != 0:
    br_stanutih_lokvi = 0
    for i in range(pocetak, zavrsni_kvadrat + 1, potenc_korak):
        if i in lokve:
            br_stanutih_lokvi += 1
            potenc_korak += 1
            break

print(potenc_korak)