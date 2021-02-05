br_znanstvenika = int(input())
ukupna_tezina = int(input())
data_tezina = int(input())
kirk_tezina = int(input())


if br_znanstvenika < 9:
    ukupna_tezina += data_tezina + kirk_tezina
    br_znanstvenika += 2

elif br_znanstvenika == 9:
    ukupna_tezina += min(data_tezina, kirk_tezina)
    br_znanstvenika += 1

print(br_znanstvenika)
print(ukupna_tezina)