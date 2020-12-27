duljina_niza_znamenaka = int(input())
pocetni_niz = [int(i) for i in input().split()]
mirkovo_zaokruzivanje = [int(i) for i in input().split()]
slavkovo_zaokruzivanje = [0] * duljina_niza_znamenaka

for i in reversed(range(duljina_niza_znamenaka)):
    if mirkovo_zaokruzivanje[i] and pocetni_niz[i] % 2 == 0:
        j = i + 1
        while j < duljina_niza_znamenaka and not mirkovo_zaokruzivanje[j] and pocetni_niz[j] % 2 == 0:
            slavkovo_zaokruzivanje[j] = 1
            j += 1
        if j < duljina_niza_znamenaka and not mirkovo_zaokruzivanje[j]:
            slavkovo_zaokruzivanje[j] = 1

    if not mirkovo_zaokruzivanje[i] and pocetni_niz[i] % 2 != 0:
        j = i + 1
        while j < duljina_niza_znamenaka and pocetni_niz[j] % 2 != 0:
            j += 1
        if j < duljina_niza_znamenaka and pocetni_niz[j + 1] % 2 != 0:
            slavkovo_zaokruzivanje[j - 1] = 1

for i in range(duljina_niza_znamenaka):
    if i == 0 and not mirkovo_zaokruzivanje[i] and pocetni_niz[i] % 2 == 1:
        slavkovo_zaokruzivanje[i] = 1

print(*slavkovo_zaokruzivanje, sep=" ")
