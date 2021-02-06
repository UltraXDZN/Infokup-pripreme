broj = int(input())

sibice_value = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

glavni_brojac = 0
for i in range(broj):
    broj_string = str(i+1)
    brojac_sibica = 0
    for j in range(len(broj_string)):
        trenutna_sibica = int(broj_string[j])
        for k in sibice_value:
            if trenutna_sibica == k:
                brojac_sibica += sibice_value[k]
                glavni_brojac += sibice_value[k]
                break


print(brojac_sibica)
print(glavni_brojac)