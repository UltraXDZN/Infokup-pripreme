broj = "".join([x[-1] for x in input().split()])
dobitci = [input() for i in range(3)]

for dobitak in dobitci:
    vrste = {
        "I. vrsta": dobitak == broj,
        "II. vrsta": dobitak[1:] == broj[1:],
        "III. vrsta": dobitak[2:] == broj[2:],
        "IV. vrsta": dobitak[3:] == broj[3:],
        "V. vrsta": dobitak[4:] == broj[4:]
    }
    has_found = False
    for k, v in vrste.items():
        if v:
            print(k)
            has_found = True
            break
    if not has_found:
        print("Nedobitan")

