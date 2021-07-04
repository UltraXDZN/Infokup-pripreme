dan = int(input())
razdoblje = input()

if razdoblje == "J":
    if dan == 1:
        dan = 31
    else:
        dan -= 1
elif razdoblje == "S":
    if dan == 31:
        dan = 1
    else:
        dan += 1

print(dan)