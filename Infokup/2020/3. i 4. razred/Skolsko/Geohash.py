dimenzije = int(input())

geohash_tablica = []
uzorak_prvi = {
    0: 0,
    1: 2,
    2: 2**dimenzije,
    3: 2**dimenzije +2
}
uzorak_drugi = {
    0: 2,
    1: -2,
    2: 2,
    3: 2
}

for i in range(2**dimenzije // 2):
    novi_red = []
    rj = ""
    for j in range(2**dimenzije // 2):
        if i == 0:
            novi_red.append(uzorak_prvi[j])

        elif i % 2 == 0 and i > 0:
            if j < 3:
                rj += f" {geohash_tablica[i-2][j+1] + uzorak_drugi[j]} |"
                novi_red.append(geohash_tablica[i-2][j+1] + uzorak_drugi[j])
            else:
                rj += f" {novi_red[-1] + uzorak_drugi[j]} |"
                novi_red.append(novi_red[-1] + uzorak_drugi[j])
        else:
            novi_red.append(geohash_tablica[i-1][j] + 1)

    geohash_tablica.append(novi_red)


for redak in geohash_tablica:
    novi_red = list(redak)
    for broj in redak:
        novi_red.append(broj + 32)
    redak = novi_red
    print(*redak)