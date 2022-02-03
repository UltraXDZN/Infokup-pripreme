rijec = input()
a = [input() for i in range(int(input()))]


for r in a:
    ps = 0
    lokacije = []
    if r in rijec:
        print("DA")
    else:
        for slovo in r:
            if slovo in rijec:
                if len(lokacije) > 1:
                    lokacije.append(rijec[lokacije[-1]+1::].find(slovo) + lokacije[-1]+1)
                else:
                    lokacije.append(rijec.find(slovo))
            else:
                print("NE")
                break
        for i in range(len(lokacije)-1):
            if ps != 0 and ps != lokacije[i+1] - lokacije[i]:
                print("NE")
                ps = 0
                break
            ps = lokacije[i+1] - lokacije[i]
        if ps != 0:
            print("DA")