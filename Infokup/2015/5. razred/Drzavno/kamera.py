vidno_polje = [int(i) for i in input().split()]
broj_vozila = int(input())
velicine_vozila = [int(i) for i in input().split()]


def pozicije(vozila, broj_manje_izv):
    lista_pos = []
    tren_pozicija = 0
    for i in range(broj_vozila - broj_manje_izv):
        lista_pos.append([tren_pozicija, vozila[i]])
        tren_pozicija += vozila[i]
    return lista_pos


for i in range(broj_vozila):
    brojac = []
    nove_pos = pozicije(velicine_vozila, i)
    nove_pos_kopija = nove_pos[:]
    for j in range(len(nove_pos)):
        if nove_pos_kopija[j][0] >= vidno_polje[0] and nove_pos_kopija[j][0] < vidno_polje[1] or nove_pos_kopija[j][1] >= vidno_polje[1] and sum(nove_pos_kopija[j]) > vidno_polje[0]:
            brojac.append(nove_pos_kopija[j][1])

    print(len(brojac))
    velicine_vozila.remove(velicine_vozila[0])
