god = input()
stoljece = [god[i] for i in range(len(god) // 2)]
print((0 if god[-1] == "0" else 1) + int("".join(stoljece)))
