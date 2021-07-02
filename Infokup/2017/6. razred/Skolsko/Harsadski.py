broj = input()

if (int(broj) % 42) == 0:
    print(sum(int(znamenka) for znamenka in broj))
else:
    print("ARTHUR")
