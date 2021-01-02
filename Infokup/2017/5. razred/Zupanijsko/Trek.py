pocetni_broj = int(input())
zavrsni_broj = int(input())

brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

brojac = 0
for broj in range(pocetni_broj, zavrsni_broj):
    if broj < 8:
        brojac += 10
    elif zavrsni_broj > 8:
        brojac += 30
    else:
        brojac += 20

print(brojac)