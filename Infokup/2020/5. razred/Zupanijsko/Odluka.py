dan = input()
broj_objave = int(input())
razmak = int(input())  # razmak između objava

dani = {
    "PONEDJELJAK": 1,
    "UTORAK": 2,
    "SRIJEDA": 3,
    "CETVRTAK": 4,
    "PETAK": 5,
    "SUBOTA": 6,
    "NEDJELJA": 7
}

dan_br = dani[dan]

for i in range(broj_objave-1):
    dan_br += razmak

while dan_br > 7:
    dan_br -= 7

print(dan_br)