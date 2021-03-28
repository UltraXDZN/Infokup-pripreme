zadano_vrijeme = "0" + input()
if len(zadano_vrijeme) < 4:
    zadano_vrijeme += "0"

opcije_vremena = []

for i in range(1, len(zadano_vrijeme)+1):
    if int(zadano_vrijeme[:i]) <= 23 and int(zadano_vrijeme[i:i+2]) <= 59:
        if "0" not in zadano_vrijeme[-2::-i]:
            opcije_vremena.append((zadano_vrijeme[1:i], zadano_vrijeme[i:i+2]))

print(opcije_vremena)

for opcija in opcije_vremena:
    if opcija is not None:
        print(f"{opcija[0]}:{opcija[1]}")
    else:
        print("TLE")

