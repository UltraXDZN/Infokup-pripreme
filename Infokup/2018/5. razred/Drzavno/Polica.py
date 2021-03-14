broj_oznacenih_kamena = int(input())

kamenje = ["_"] * 500

najveci_br = 0
for i in range(1, broj_oznacenih_kamena + 1):
    novi_broj = int(input())
    kamenje[novi_broj] = i
    najveci_br = novi_broj if novi_broj > najveci_br else najveci_br

del kamenje[najveci_br + 1::]

broj_preslagivanja = int(input())
preslagivanja = []
for i in range(broj_preslagivanja):
    preslagivanja.append(int(input()))

for preslagivanje in preslagivanja:
    trenutno_odabrani_brojevi = []
    for i in reversed(range(len(kamenje))):
        if kamenje[i] != "_":
            trenutno_odabrani_brojevi.append(i)
            # print(trenutno_odabrani_brojevi)
            if len(trenutno_odabrani_brojevi) == preslagivanje + 1:
                # print(f"X je {preslagivanje}, zadnje kamenje je {trenutno_odabrani_brojevi})")
                trenutno_odabrani_x = []
                for j in reversed((range(i))):
                    if kamenje[j] == "_":
                        trenutno_odabrani_x.append(j)
                        # print(trenutno_odabrani_x)
                        if len(trenutno_odabrani_x) == preslagivanje + 1:
                            # print(f"X je {preslagivanje}, prednje kamenje je {trenutno_odabrani_x})")
                            for k in reversed((range(preslagivanje + 1))):
                                kamenje[trenutno_odabrani_brojevi[k]], kamenje[trenutno_odabrani_x[k]] = kamenje[
                                                                                                             trenutno_odabrani_x[
                                                                                                                 k]], \
                                                                                                         kamenje[
                                                                                                             trenutno_odabrani_brojevi[
                                                                                                                 k]]
                # print(kamenje)
                break

for kamen in kamenje:
    if kamen != "_":
        print(kamen)
