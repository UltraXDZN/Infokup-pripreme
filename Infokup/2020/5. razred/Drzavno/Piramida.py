def nadji_srednji_broj(lista_brojeva):
    return sorted(lista_brojeva)[1]


tip = int(input())

donji_red = []
for i in range(tip):
    donji_red.append(int(input()))

gornji_broj = 0

if tip == 5:
    srednji_red = []
    for i in range(tip - 2):
        srednji_red.append(nadji_srednji_broj([donji_red[i], donji_red[i + 1], donji_red[i + 2]]))
    donji_red = srednji_red

gornji_broj = nadji_srednji_broj(donji_red)

print(gornji_broj)
