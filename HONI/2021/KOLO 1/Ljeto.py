broj_zapazanja = int(input())

zapazanja = []

for i in range(broj_zapazanja):
    zapazanja.append([int(x) for x in input().split()])

timovi = {
    "Avokado": [1, 2, 3, 4],
    "Borovnice": [5, 6, 7, 8]
}
avokado_bodovi = 0
borovnice_bodovi = 0

vrijeme = [-100] * 8


def get_key(val):
    for key, value in timovi.items():
        if val in value:
            return key


u_deset_sek = False
for i in range(broj_zapazanja):
    if (zapazanja[i][0] - vrijeme[zapazanja[i][1] - 1]) <= 10:
        u_deset_sek = True
    else:
        u_deset_sek = False

    trenutni_tim = get_key(zapazanja[i][1])
    if trenutni_tim == "Avokado":
        avokado_bodovi += 100
        if u_deset_sek:
            avokado_bodovi += 50
            u_deset_sek = False
    elif trenutni_tim == "Borovnice":
        borovnice_bodovi += 100
        if u_deset_sek:
            borovnice_bodovi += 50
            u_deset_sek = False

    vrijeme[zapazanja[i][1] - 1] = zapazanja[i][0]

print(avokado_bodovi, borovnice_bodovi)
