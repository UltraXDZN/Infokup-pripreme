import sys

baza = int(input())
pocetni_broj = int(input())
zavrsni_broj = int(input())

dimenzije = 2 ** baza
geohash_tablica = [[0 for x in range(dimenzije)] for y in range(dimenzije)]
geohash_tablica_visited = [[0 for x in range(dimenzije)] for y in range(dimenzije)]


def ispisi_tablicu(tablica):
    for redak in tablica:
        for broj in redak:
            print(f"{broj:2d}", end="   ")
        print()

def pronadji_koordinate():
    r1 = c1 = 0
    r2 = c2 = 0
    for i in range(dimenzije):
        for j in range(dimenzije):
            if geohash_tablica[i][j] == pocetni_broj:
                r1, c1 = j, i
            if geohash_tablica[i][j] == zavrsni_broj:
                r2, c2 = j, i

    return [(r1, c1), (r2, c2)]

for redak in range(dimenzije):
    for stupac in range(dimenzije):
        # project full table in to one row and one colum
        bit_string = ""

        # start at center
        offset_x = offset_y = (dimenzije / 2)

        divider_x = offset_x
        divider_y = offset_y

        for value in range(baza):

            if stupac < offset_y:
                bit_string += '0'
                divider_y /= 2
                offset_y -= divider_y  # (offset_y / 2)
            else:
                bit_string += '1'
                divider_y /= 2
                offset_y += divider_y  # (offset_y / 2)

            if redak < offset_x:
                bit_string += '0'
                divider_x /= 2
                offset_x -= divider_x  # (offset_x / 2)
            else:
                bit_string += '1'
                divider_x /= 2
                offset_x += divider_x  # (offset_x / 2)

            if (value + 1) == baza:
                bit_to_int = int(bit_string, 2)
                geohash_tablica[(dimenzije - 1) - redak][stupac] = bit_to_int

ispisi_tablicu(geohash_tablica)
print()
# ispisi_tablicu(geohash_tablica_visited)

koordinate = pronadji_koordinate()

print()
print(f"Pocetna lokacija: {koordinate[0]}")
print(f"Zavrsna lokacija: {koordinate[1]}")

def min_path_sum(tablica):
    if dimenzije == 0:
        return 0

    cur = [tablica[0][0]] + [float(sys.maxsize)] * (dimenzije-1)
    for j in range(1, dimenzije):
        cur[j] = tablica[0][j] + cur[j-1]

    print(cur)
    for i in range(0, dimenzije):
        cur[i] = tablica[0][i] + cur[0]
        for j in range(1, dimenzije):
            cur[j] = tablica[i][j] + min(cur[j], cur[j-1])
        print(tablica[i][j])

    return cur[-1]

print(min_path_sum(geohash_tablica))


# susjedi_x = susjedi_y = []
# zbroj = 0

# def pronadji_susjede(a1, b1, a2, b2):
#     dir_x = [-1, 1, 0, 0]
#     dir_y = [0, 0, 1, -1]
#
#     for i in range(4):
#         xx = a1 + dir_x[i]
#         yy = b1 + dir_y[i]
#         if xx < 0 or yy < 0:
#             continue
#         if xx >= dimenzije or yy >= dimenzije:
#             continue
#         if geohash_tablica_visited[xx][yy] == 1:
#             continue
#
#         susjedi_x.pop(xx)
#         susjedi_y.pop(yy)
#         geohash_tablica_visited[xx][yy] = 1
#         zbroj += geohash_tablica[xx][yy]
