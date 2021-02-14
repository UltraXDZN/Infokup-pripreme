vrijendosti = ["7", "8", "9", "X", "D", "B", "K", "A"]
boje = ["P", "K", "H", "T"]

ruka = []

for i in range(8):
    value = input().split()
    ruka.append(value)

rjesenje = []
for i in reversed(range(8)):
    for j in reversed(range(8)):
        for k in reversed(range(min(i, j), 8)):
            if ruka[i][1] == ruka[j][1] == ruka[k][1]:
                if vrijendosti.index(ruka[k][0]) > vrijendosti.index(ruka[j][0]) > vrijendosti.index(ruka[i][0]):
                    rjesenje.append(["1", ruka[i][1], ruka[i][0]])
            for l in reversed(range(8)):
                if ruka[i][0] == ruka[j][0] == ruka[k][0] == ruka[l][0]:
                    if ruka[i][1] != ruka[j][1] != ruka[k][1] != ruka[l][1]:
                        rjesenje.append(["2", ruka[i][0]])

myFinallist = []
for i in rjesenje:
    if i not in myFinallist:
        myFinallist.append(i)
        print(*i)

# print(ruka)
