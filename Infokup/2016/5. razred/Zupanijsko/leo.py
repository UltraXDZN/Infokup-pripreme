xTrenutniKat = int(input())
zeljeniKatLeo = int(input())
zeljeniKatKiki = int(input())

if xTrenutniKat < zeljeniKatLeo:
    print("G")
else:
    print("D")

xTrenutniKat = abs(xTrenutniKat - zeljeniKatLeo)
print(xTrenutniKat)
print(abs(zeljeniKatKiki - zeljeniKatLeo) + xTrenutniKat)


