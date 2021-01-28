datum = int(input())
sat_koncerta = int(input())
vrijeme_leta = int(input())
vremenska_razlika = int(input())

novi_datum = datum
potrebno_vrijeme = sat_koncerta - vrijeme_leta + vremenska_razlika

if potrebno_vrijeme > 24:
    datum += 1
    potrebno_vrijeme -= 24

print(datum)
print(potrebno_vrijeme)