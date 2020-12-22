rjesenja_dict = {
    1: "***\n*O*\n***",
    2: "O**\n***\n**O",
    3: "O**\n*O*\n**O",
    4: "O*O\n***\nO*O",
    5: "O*O\n*O*\nO*O",
    6: "OOO\n***\nOOO",
}

gornji_broj = 7 - int(input())
print(f"{gornji_broj}\n{rjesenja_dict[gornji_broj]}")
