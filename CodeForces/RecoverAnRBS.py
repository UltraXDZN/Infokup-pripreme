for i in range(int(input())):
    rbs = input()
    bc, qmc, ss = 0, 0, True  # bc - bracket counter, qmc - question marks counter, ss - single solution
    for i in range(len(rbs)):
        if rbs[i] == "(":
            bc += 1
        elif rbs[i] == ")":
            bc -= 1
        else:
            qmc += 1
        fl = len(rbs) - i - 1  # fl - from last
        lowest, highest = max((bc + qmc) % 2, bc - qmc), min(bc + qmc, fl - abs(fl % 2 - (bc + qmc) % 2))

        if highest == lowest and qmc:
            if qmc != abs(highest - bc):
                ss = False
            qmc = 0
            bc = highest

    print(["NO", "YES"][ss])
