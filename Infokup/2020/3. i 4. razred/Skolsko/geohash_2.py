baza = int(input())

dimenzije = 2 ** baza
geohash_tablica = [[0 for x in range(dimenzije)] for y in range(dimenzije)]

for redak in range(dimenzije):
    for stupac in range(dimenzije):
        # project full table in to one row and one colum
        bit_string = ""

        # start at center
        offset_x = (dimenzije / 2)
        offset_y = offset_x

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

for redak in geohash_tablica:
    print(*redak)
