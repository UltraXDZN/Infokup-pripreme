dan = int(input())
mjesec = int(input())

if (dan >= 21 or dan < 20) and (mjesec == 3 or mjesec == 4):
    print("OVAN")
elif (dan >= 21 or dan < 20) and (mjesec == 4 or mjesec == 5):
    print("BIK")
elif (dan >= 21 or dan < 20) and (mjesec == 5 or mjesec == 6):
    print("BLIZANCI")
elif (dan >= 21 or dan < 20) and (mjesec == 6 or mjesec == 7):
    print("RAK")
elif (dan >= 21 or dan < 21) and (mjesec == 7 or mjesec == 8):
    print("LAV")
elif (dan >= 22 or dan < 22) and (mjesec == 8 or mjesec == 9):
    print("DJEVICA")
elif (dan >= 23 or dan < 22) and (mjesec == 9 or mjesec == 10):
    print("VAGA")
elif (dan >= 23 or dan < 22) and (mjesec == 10 or mjesec == 11):
    print("SKORPION")
elif (dan >= 23 or dan < 21) and (mjesec == 11 or mjesec == 12):
    print("STRIJELAC")
elif (dan >= 22 or dan < 20) and (mjesec == 12 or mjesec == 1):
    print("JARAC")
elif (dan >= 21 or dan < 19) and (mjesec == 1 or mjesec == 2):
    print("VODENJAK")
elif (dan >= 20 or dan < 20) and (mjesec == 2 or mjesec == 3):
    print("RIBE")