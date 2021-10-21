# '.' -> bijelo polje
# '#' -> crno polje

dimenzija_x, dimenzija_y = [int(dimenzija) for dimenzija in input().split()]

plocice = []
for i in range(dimenzija_x):
    plocice.append(input())

uzorak = []
uzorak_pronadjen = False
for redak in plocice:
    uzorak_x, uzorak_y = ""
    for i in range(0, len(redak) + 1):
        if redak.count(uzorak_x) < (len(redak) // redak.count(uzorak_x)):
            uzorak_x = uzorak_x[0:len(uzorak_x) - 1]
            break
        uzorak_x = redak[0: i]

    if uzorak_x not in uzorak:
        uzorak.append(uzorak_x)

print(len(uzorak), len(uzorak[0]))
