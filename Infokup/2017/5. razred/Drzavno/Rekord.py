broj_bacanja = int(input())
bacanja = []

for i in range(broj_bacanja):
    bacanja.append(float(input()))
rekordi = {
    66.18: "PB",
    71.53: "OR",
    72.28: "WR"
}

for i in range(broj_bacanja - 1):
    for k, v in rekordi.items():
        print(bacanja[i])
        if bacanja[i] >= k:
            print(rekordi[k])
            break
        else:
            print(bacanja[i])
            break
