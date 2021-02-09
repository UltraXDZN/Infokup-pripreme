unos = input()

for i in range(len(unos)):
    if len(unos) % 4 != 0:
        unos += "X"
    else:
        break

slova = []
for i in range(0,len(unos)-3, 4):
    slova.append([unos[i], unos[i+1], unos[i+2], unos[i+3]])


for slovo in slova:
    print(slovo)

kriptirana_poruka = ""

for i in range(4):
    for slovo in slova:
        if i < len(slovo):
            kriptirana_poruka += slovo[i]
        else:
            break
print(kriptirana_poruka)