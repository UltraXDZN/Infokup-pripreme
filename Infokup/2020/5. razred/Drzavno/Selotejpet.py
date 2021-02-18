broj_komada = int(input())
podjela = int(input())

daska = [""] * podjela

komadi_limiti = []
for i in range(broj_komada):
    temp_unos = [int(num) for num in input().split()]
    komadi_limiti.append(temp_unos)

for i in range(len(komadi_limiti)):
    temp_komad = komadi_limiti[i]
    temp_komad = [num for num in range(temp_komad[0]-1, temp_komad[-1])]
    for num in temp_komad:
        daska[num] += str(i+1)

temp_len = []
for komad in daska:
    temp_len.append(len(komad))
print(max(temp_len))

# prvi_komad = 0
# for komad in daska:
#     if komad != "":
#         print(komad[0])
#         break

