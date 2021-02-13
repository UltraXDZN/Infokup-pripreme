vrijendosti = ["7", "8", "9", "X", "D", "B", "K", "A"]
boje = ["P", "K", "H", "T"]

ruka = []

for i in range(8):
    value = input().split()
    ruka.append(value)

for i in reversed(range(8)):
    for j in reversed(range(8)):
        for k in range(8):
            if ruka[i][1] == ruka[j][1] == ruka[k][1]:
                if vrijendosti.index(ruka[k][0]) > vrijendosti.index(ruka[j][0]) > vrijendosti.index(ruka[i][0]):
                    print("1", ruka[i][1], ruka[i][0])

    # if ruka[i][1] == ruka[i+1][1] == ruka[i+2][1]:
    #     print("jej 1")
    #     for j in range(len(vrijendosti)-2):
    #         print(ruka[i][0], vrijendosti[j])
    #         print(ruka[i + 1][0], vrijendosti[j + 1])
    #         print(ruka[i + 2][0], vrijendosti[j + 2])
    #         if ruka[i][0] == vrijendosti[j] and ruka[i+1][0] == vrijendosti[j+1] and ruka[i+2][0] == vrijendosti[j+2]:
    #             print("jej 2")
    #         print("-------------")

print(ruka)
