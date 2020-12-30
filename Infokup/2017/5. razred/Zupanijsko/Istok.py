gledamo = input()
strana_svijeta = int(input())

strane = [("I", "Z"), ("S", "J")]
strane_0 = strane[0]
strane_1 = strane[1]

if strana_svijeta == 2:
    if (gledamo in strane_0):
        if (strane_0[strane_0.index(gledamo)] == -1):
            print(strane_0[0])
        else:
            print(strane_0[1])
    else:
        if (strane_1[strane_1.index(gledamo)] == -1):
            print(strane_1[0])
        else:
            print(strane_1[1])

if strana_svijeta == 1:
    if (gledamo in strane_0):
        print(strane_1[strane_0.index(gledamo) - 1])
    else:
        print(strane_0[strane_1.index(gledamo)])

if strana_svijeta == 0:
    if (gledamo in strane_0):
        print(strane_1[strane_0.index(gledamo)])
    else:
        print(strane_0[strane_1.index(gledamo) - 1])
