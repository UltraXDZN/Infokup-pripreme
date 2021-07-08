prednost = int(input())
broj_bacanja = int(input())



bacanja = []
konos_bodovi = 0
kang_bodovi = 0

konos_runde = 0
kang_runde = 0

for i in range(broj_bacanja):
    bacanje = [int(broj) for broj in input().split()]
    bacanja.append(bacanje)
    if bacanje[0] > bacanje[1]:
        konos_bodovi += sum(bacanje)
        konos_runde += 1
    elif bacanje[1] > bacanje[0]:
        kang_bodovi += sum(bacanje)
        kang_runde += 1

if prednost % 2 == 0:
    print("KANG")
else:
    print("KONOS")
print(konos_runde, kang_runde)
print(konos_bodovi, kang_bodovi)