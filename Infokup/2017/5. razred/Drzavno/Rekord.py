broj_bacanja = int(input())
bacanja = []

for i in range(broj_bacanja):
    bacanja.append(float(input()))
rekordi = {
    66.18: "PB",
    71.53: "OR",
    72.28: "WR"
}

for i in range(broj_bacanja):
    jeIspisao = False
    for k, v in reversed(rekordi.items()):
        if k < bacanja[i]:
            print(rekordi[k])
            jeIspisao = True
            break

    if not jeIspisao:
        print(bacanja[i])
