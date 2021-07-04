bodovi = int(input())
ocjena = int(input())

bodovna_lista = {
    2: 45,
    3: 60,
    4: 75,
    5: 90
}

dobivena_ocjena = 1
for k, v in bodovna_lista.items():
    if bodovi > v:
        dobivena_ocjena = k

print(dobivena_ocjena)
bodovi_do_ocjene = bodovna_lista[ocjena] - bodovi
if bodovi_do_ocjene > 0:
    print(bodovi_do_ocjene)
else:
    print("REBEKA")
