broj_ucenika = int(input())

parni_ucenici = []
neparni_ucenici = []

for i in range(1, broj_ucenika+1):
    ocjena = int(input())
    if i % 2 == 0:
        parni_ucenici.append(ocjena)
    else:
        neparni_ucenici.append(ocjena)

prosjek_parnih = sum(parni_ucenici) / len(parni_ucenici)
prosjek_neparnih = sum(neparni_ucenici) / len(neparni_ucenici)


rjesenje = ""
if prosjek_neparnih > prosjek_parnih:
    rjesenje = "N"
elif prosjek_parnih > prosjek_neparnih:
    rjesenje = "P"
else:
    rjesenje = "PN"

print(f"{round(prosjek_parnih, 2)}")
print(f"{round(prosjek_neparnih, 2)}")
print(rjesenje)