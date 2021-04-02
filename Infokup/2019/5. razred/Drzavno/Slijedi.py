broj_zadataka = int(input())
broj_dijelova = int(input())

rjesenja_zadataka = []


def slijedi_gresku(rjesenje_prvo, rjesenje_trenutno):
    if (rjesenje_prvo[0] - rjesenje_prvo[1]) == (rjesenje_trenutno[0] - rjesenje_trenutno[1]):
        #print(f"{rjesenje_prvo[0]} - {rjesenje_prvo[1]} = {rjesenje_trenutno[0]} - {rjesenje_trenutno[1]}")
        return 1
    return 0

for i in range(broj_zadataka):
    zadatak = []
    for j in range(broj_dijelova):
        dio_zadatka = [int(broj) for broj in input().split()]
        zadatak.append(tuple(dio_zadatka))
    rjesenja_zadataka.append(zadatak)

bodovi = []

for zadatak in rjesenja_zadataka:
    bodovi_zadatka = 0
    krivo_rjeseni_zadatak = None
    for rjesenje in range(len(zadatak)):
        if krivo_rjeseni_zadatak is None:
            if zadatak[rjesenje][0] == zadatak[rjesenje][1]:
                bodovi_zadatka += 1
            else:
                krivo_rjeseni_zadatak = rjesenje
        else:
            trenutni_bod = slijedi_gresku(zadatak[krivo_rjeseni_zadatak], zadatak[rjesenje])
            if trenutni_bod == 1:
                bodovi_zadatka += trenutni_bod
                continue
            else:
                break

    bodovi.append(bodovi_zadatka)

print(sum(bodovi))
