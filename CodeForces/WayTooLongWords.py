rijeci = []
for i in range(int(input())):
    rijeci.append(input())

for rijec in rijeci:
    if len(rijec) > 10:
        print(f"{rijec[0]}{len(rijec) - 2}{rijec[-1]}")
    else:
        print(rijec)
