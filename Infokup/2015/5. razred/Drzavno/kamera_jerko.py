vidno_polje = [int(i) for i in input().split()]
broj_vozila = int(input())
duljine_vozila = [int(i) for i in input().split()]
nova_vozila = []


def mici_petice(uda, dv, nv, vp):
    """
    Funkcija mici_petice prima sljedeće parametre:
    :param uda: udaljenost
    :param dv: duljina vozila
    :param nv: nova vozila
    :param vp: vidno polje

    Funkcija vraća listu vozila bez hitnih.
    :return: lista nova vozila
    """
    for v in dv:
        uda += v
        if not (uda > vp[0] and v == 5):
            nv.append(v)
    return nv


duljine_vozila = mici_petice(0, duljine_vozila, nova_vozila, vidno_polje)

while len(duljine_vozila):
    if duljine_vozila[0] == 5:
        del duljine_vozila[0]
        continue
    vozila_u_kameri = []

    for j in range(len(duljine_vozila)):
        if len(vozila_u_kameri) == 0 and sum(duljine_vozila[:j + 1]) > vidno_polje[0]:
            vozila_u_kameri.append(duljine_vozila[j])
            continue

        if len(vozila_u_kameri) > 0 and sum(duljine_vozila[:j]) < vidno_polje[1]:
            vozila_u_kameri.append(duljine_vozila[j])

    del duljine_vozila[0]
    print(len(vozila_u_kameri))
