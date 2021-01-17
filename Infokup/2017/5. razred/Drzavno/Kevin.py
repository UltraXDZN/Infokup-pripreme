broj_nestanaka_struje = int(input())
vrijeme = []

for i in range(broj_nestanaka_struje):
    vrijeme.append([int(i) for i in input().split()])

pocetno_vrijeme = vrijeme[0]
vrijeme_na_satu = 0

for i in range(0, broj_nestanaka_struje, 2):
    if (vrijeme[i][1] > vrijeme[i-1][1]):
        vrijeme_na_satu += 60 - vrijeme[i][1]
    vrijeme_na_satu += vrijeme[i][1] - vrijeme[i-1][1]
    if (i+1 <= len(vrijeme)):
        pocetno_vrijeme[1] += vrijeme[i+1][1]

print(abs(vrijeme_na_satu))
print(*pocetno_vrijeme, sep=" ")