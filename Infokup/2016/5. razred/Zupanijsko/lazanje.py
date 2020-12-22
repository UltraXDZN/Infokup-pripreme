brojGostiju = int(input())
brojTomaz = 0
brojMate = 0



for i in range(brojGostiju):
    glas = input()
    if glas == "T":
        brojTomaz += 1
    else:
        brojMate += 1

pobjednik = brojTomaz if brojTomaz > brojMate else brojMate

print(pobjednik)
print(brojGostiju - pobjednik)
