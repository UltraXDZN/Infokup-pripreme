pozicije_kockice = {
    1: "***\n*O*\n***",
    2: "O**\n***\n**O",
    3: "O**\n*O*\n**O",
    4: "O*O\n***\nO*O",
    5: "O*O\n*O*\nO*O",
    6: "OOO\n***\nOOO",
}

broj_kockice_gore = 7 - int(input())
print(f"{broj_kockice_gore}\n{pozicije_kockice[broj_kockice_gore]}")
