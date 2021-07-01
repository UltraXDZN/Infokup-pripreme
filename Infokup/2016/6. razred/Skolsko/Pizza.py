broj_osoba = int(input())
broj_komada = int(input())


rjesenje = broj_komada % broj_osoba

if rjesenje == 0:
    rjesenje = broj_osoba

print(rjesenje)