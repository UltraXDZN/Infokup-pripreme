broj_utakmica = int(input())

rez_utakmica = []
for i in range(broj_utakmica):
    rez_utakmica.append([int(broj) for broj in input().split()])

izgubljeni_bodovi = 0
for rez in rez_utakmica:
    if rez[3] > rez[2] and rez[1] < rez[0]:
        izgubljeni_bodovi += 3
    elif rez[3] > rez[2] and rez[1] == rez[0]:
        izgubljeni_bodovi += 1
    elif rez[3] == rez[2] and rez[1] < rez[0]:
        izgubljeni_bodovi += 2

print(izgubljeni_bodovi)
