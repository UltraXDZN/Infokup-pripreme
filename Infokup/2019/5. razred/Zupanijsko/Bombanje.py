broj_rundi_uk = int(input())
pocetni_broj_bombona = int(input())

igracevi_brojevi = []
generatorovi_brojevi = []

for i in range(broj_rundi_uk):
    igracevi_brojevi.append(int(input()))
    generatorovi_brojevi.append(int(input()))

brojevi = [*zip(igracevi_brojevi, generatorovi_brojevi)]
zbroj = 0
increment = 0
decrement = 1

for i in range(len(brojevi)):
    if brojevi[i][0] == brojevi[i][1]:
        zbroj += pocetni_broj_bombona + increment
        increment += 1
    else:
        zbroj -= decrement
        if zbroj < 0:
            zbroj = 0
        decrement += 2

print(increment)
print(zbroj)