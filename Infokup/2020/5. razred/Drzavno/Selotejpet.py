broj_komada = int(input())
podjela = int(input())

komadi_limiti = []
for i in range(broj_komada):
    temp_unos = [int(num) for num in input().split()]
    komadi_limiti.append(temp_unos)

daska = [""] * podjela

for broj, polozaj in enumerate(komadi_limiti, 1):
    oznaka = f'#{broj}'
    pocetak = polozaj[0] - 1
    duljina = polozaj[1] - pocetak
    for i in range(duljina):
        daska[pocetak + i] += oznaka

daska_bez_hasha = [s.replace("#", "") for s in daska if "#" in s]
max_duljina = max(len(ozn) for ozn in daska_bez_hasha)
print(max_duljina)

najmanja_oznaka = broj_komada
for i in range(broj_komada - 1, 0, -1):
    l = []
    oznaka = f'#{i}'
    for ozn in daska:
        if oznaka in ozn:
            l.append(ozn)
    if all([o.endswith(oznaka) for o in l]):
        najmanja_oznaka = int(oznaka[-1])

print(najmanja_oznaka)
