duljina_niza_znamenaka = int(input())
pocetni_niz = input().replace(" ", "")
mirkovo_zaokruzivanje = input().replace(" ", "")

zaokruzeni_brojevi = []

for i in range(len(pocetni_niz)):
    if mirkovo_zaokruzivanje[i] == "1":
        zaokruzeni_brojevi.append(i)

slavkovo_zaokruzivanje = [0] * duljina_niza_znamenaka
trenutni_broj = ""
for i in range(len(pocetni_niz)-1, -1, -1):
    trenutni_broj += pocetni_niz[i]
    if int(pocetni_niz[i]) % 2 != 0 and i not in zaokruzeni_brojevi and i+1 not in zaokruzeni_brojevi and int(trenutni_broj) % 2 != 0:
        slavkovo_zaokruzivanje[i] = 1
    else:
        trenutni_broj = ""

print(slavkovo_zaokruzivanje)
#got to finish 2/3 done
