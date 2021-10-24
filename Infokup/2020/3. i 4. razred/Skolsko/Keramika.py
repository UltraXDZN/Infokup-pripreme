# '.' -> bijelo polje
# '#' -> crno polje

dimenzija_x, dimenzija_y = [int(dimenzija) for dimenzija in input().split()]

plocice = []
for i in range(dimenzija_x):
    plocice.append(input())

uzorak = []
uzorak_pronadjen = False
for redak in plocice:
    uzorak_x = ""
    if len(redak) % 2 != 0:
        redak = redak + redak[1]
    for i in range(0, len(redak) + 1):

        if len(uzorak_x) == (len(redak) // redak.count(uzorak_x)) \
                and len(uzorak_x) != 0 \
                or len(uzorak_x) >= len(redak) - 1:
            uzorak_x = uzorak_x[0:len(uzorak_x)]
            break
        uzorak_x = redak[0: i]

    redak = redak[0:-1]
    if uzorak_x not in uzorak:
        uzorak.append(uzorak_x)

print(len(uzorak), len(uzorak[0]))