redovi = int(input())
stupci = int(input())

tablica = []

for i in range(redovi):
    if i == 0 or i == redovi-1:
        tablica.append(('b#' * stupci).split("#"))
    else:
        redak_tr = ['b']
        for j in range(stupci-2):
            redak_tr.append('n')
        redak_tr.append('b')
        tablica.append(redak_tr)

obojana_polja = 0
for i in range(len(tablica)):
    for polje in tablica[i]:
        if polje == 'b':
            obojana_polja += 1

print(obojana_polja)
