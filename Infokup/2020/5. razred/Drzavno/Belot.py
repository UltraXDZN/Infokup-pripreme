vrijendosti = ["7", "8", "9", "X", "D", "B", "K", "A"]
boje = ["P", "K", "H", "T"]

ruka = []

for i in range(8):
    value = input().split()
    ruka.append(value)

rjesenje = []
dvojke = []
for i in reversed(range(8)):
    for j in reversed(range(8)):
        for k in reversed(range(8)):
            if ruka[i][1] == ruka[j][1] == ruka[k][1]:
                if vrijendosti.index(ruka[k][0]) - vrijendosti.index(ruka[j][0]) == 1 and vrijendosti.index(ruka[j][0]) - vrijendosti.index(ruka[i][0]) == 1:
                    rjesenje.append(["1", ruka[i][1], ruka[i][0]])
                    break

            for l in reversed(range(8)):
                if len({ruka[i][0], ruka[j][0], ruka[k][0], ruka[l][0]}) <= 1:
                    if len(list(set([ruka[i][1], ruka[j][1], ruka[k][1], ruka[l][1]]))) == 4 and sorted([ruka[i][1], ruka[j][1], ruka[k][1], ruka[l][1]]) not in dvojke:
                        rjesenje.append(["2", ruka[i][0]])
                        dvojke.append(sorted([ruka[i][1], ruka[j][1], ruka[k][1], ruka[l][1]]))
                        break
myFinallist = []
for i in rjesenje:
    if i not in myFinallist:
        myFinallist.append(i)
        print(*i)

