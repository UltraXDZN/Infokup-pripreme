duljina_niza_znamenaka = int(input())
pocetni_niz = [int(i) for i in input().split()]
mirkovo_zaokruzivanje = [int(i) for i in input().split()]

zaokruzeni_brojevi = []
parni = [int(i) for i in range(len(pocetni_niz)) if i % 2 == 0]
neparni = [int(i) for i in range(len(pocetni_niz)) if i % 2 != 0]

for i in range(len(mirkovo_zaokruzivanje)):
    if mirkovo_zaokruzivanje[i] == 1:
        zaokruzeni_brojevi.append(i)

print(zaokruzeni_brojevi)
print(parni)
print(neparni)
