zadano_vrijeme = input()

opcije_vremena = []
if len(zadano_vrijeme) == 1:
    opcije_vremena.append((0, int(zadano_vrijeme)))
    opcije_vremena.append((int(zadano_vrijeme), 0))
elif len(zadano_vrijeme) == 2:
    opcije_vremena.append((0, int(zadano_vrijeme)))
    opcije_vremena.append((int(zadano_vrijeme[0]), int(zadano_vrijeme[1])))
    opcije_vremena.append((int(zadano_vrijeme), 0))

else:
    sati, minute = 0, 0
    sati = int(zadano_vrijeme[0:1]) if int(zadano_vrijeme[0:2]) > 23 else int(zadano_vrijeme[0:2])
    minute = int(zadano_vrijeme.replace(str(sati), ""))
    if 0 > minute > 59:
        opcije_vremena(None)
    opcije_vremena.append((sati, minute))

for opcija in opcije_vremena:
    if opcija is not None:
        print(f"{opcija[0]}:{opcija[1]}")
    else:
        print("TLE")

