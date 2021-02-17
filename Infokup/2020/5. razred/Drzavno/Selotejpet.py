broj_komada = int(input())
podjela = int(input())

daska_za_cvarke = [[]] * podjela

komadi_limiti = []
for i in range(broj_komada):
    temp_unos = input().split()
    komadi_limiti.append(temp_unos)

for i in range(len(komadi_limiti)):
    for j in range(int(komadi_limiti[i][0]), int(komadi_limiti[i][1])+1):
        print(j)
        daska_za_cvarke[j].append(f"#{i+1}")
    print("--------")

print(daska_za_cvarke)