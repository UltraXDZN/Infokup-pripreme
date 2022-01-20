def turn_to_zero(a):
    c = 0
    if "11" in a:  # LIJEVO
        b = a[:a.find("11") + a.count("1")].replace("1", "2").replace("0", "1").replace(
            "2", "0")
        b += a[a.find("11") + a.count("1"):]
        a = b
        c = 1
    return [a, c]


n = int(input())
niz = input()
ct = niz.count("010")
niz = niz.replace("010", "000")

while niz.count("1") > 0:
    niz_a = turn_to_zero(niz[:(len(niz) // 2)])
    niz_b = turn_to_zero("".join(list(reversed(niz[(len(niz) // 2):]))))
    niz = niz_a[0] + "".join(list(reversed(niz_b[0])))
    ct += niz_a[1] + niz_b[1]

print(ct)
