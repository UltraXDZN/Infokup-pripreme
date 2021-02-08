broj_predmeta = int(input())
odabrani_predmet = int(input())



starosti_liste = []
for i in range(broj_predmeta):
    starosti = []
    for j in range(3):
        starosti.append(int(input()))
    starosti_liste.append(starosti)

tjedan = 7
mjesec = 28
godina = 336
zbroj = 0
for predmet in starosti_liste:
    trenutni_zbroj = (predmet[0] * godina) + (predmet[1] * mjesec) + (predmet[2] * tjedan)
    if starosti_liste.index(predmet) == odabrani_predmet-1:
        print(trenutni_zbroj)
    zbroj += trenutni_zbroj

print(zbroj)
