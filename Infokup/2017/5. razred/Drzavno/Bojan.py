broj_stupaca = int(input())
stupci = [int(i) for i in input().split()]
broj_bojanja_zida = int(input())
koraci = []
for i in range(broj_bojanja_zida):
    koraci.append([int(i) for i in input().split()])

# print(koraci)
# print(stupci)
boja_na_zidu = [0] * broj_stupaca
for korak in koraci:
    # print(f"---------------------------------------------------------- {koraci.index(korak)} ")
    trenutna_boja = korak[2]
    trenutna_lokacija = korak[0]-1
    promijeni_smjer = False
    while trenutna_boja != 0:
        # print(f"--------------------------------------- {trenutna_boja}, {trenutna_lokacija}, {promijeni_smjer} pocetak")
        if trenutna_lokacija >= korak[1] or trenutna_lokacija < korak[0]-1:
            promijeni_smjer = not promijeni_smjer
            if promijeni_smjer:
                trenutna_lokacija -= 1
            else:
                trenutna_lokacija += 1
        trenutna_boja -= 1
        boja_na_zidu[trenutna_lokacija] += 1
        #trenutna_lokacija += 1

        if promijeni_smjer:
            trenutna_lokacija -= 1
        else:
            trenutna_lokacija += 1
        # print(f"--------------------------------------- {trenutna_boja}, {trenutna_lokacija}, {promijeni_smjer} kraj")
print(*boja_na_zidu)
