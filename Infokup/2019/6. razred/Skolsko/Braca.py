prvi_brat = input()
drugi_brat = input()

braca = {
    "V": [0, "VEDRAN"],
    "M": [1, "MARIN"],
    "S": [2, "STJEPAN"]
}

for v in braca.values():
    if v[0] == min(braca[prvi_brat][0], braca[drugi_brat][0]):
        print(v[1])
