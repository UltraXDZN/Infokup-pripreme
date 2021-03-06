pocetni_lopoc = int(input())
posljednji_lopoc = int(input())


def pronadji_put(graf, pocetak, kraj, put=[]):
    put += [pocetak]
    if pocetak == kraj:
        return put
    if pocetak not in graf:
        return None
    for node in graf[pocetak]:
        if node not in put:
            print(graf[pocetak][graf[pocetak].index(node)])
            novi_put = pronadji_put(graf, node, kraj, put)
            if novi_put:
                return novi_put
    return None


lopoci = {
    1: [2, 6, 7],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [1, 6],
    7: [1]
}

print(len(pronadji_put(lopoci, pocetni_lopoc, posljednji_lopoc, []))-1)
print(pronadji_put(lopoci, pocetni_lopoc, posljednji_lopoc, []))
