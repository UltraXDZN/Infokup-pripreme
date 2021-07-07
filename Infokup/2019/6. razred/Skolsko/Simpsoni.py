prednost = int(input())
broj_bacanja = int(input())

bodovi = []

for i in range(broj_bacanja):
    bodovi.append([int(broj) for broj in input().split()])

if prednost % 2 == 0:
    print("KANG")
else:
    print("KONOS")