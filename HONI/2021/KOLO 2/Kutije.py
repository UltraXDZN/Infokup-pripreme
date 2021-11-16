n, m, q = map(int, input().split())

kutije = {}

for i in range(n):
    kutije[i+1] = []

razvstavanja = []
for i in range(m):
    razvstavanja.append([int(x) for x in input().split()])

pitanja = []
for i in range(q):
    pitanja.append([int(x) for x in input().split()])


for i in range(n):
    for j in range(m):
        je_i_dodan = False
        for num in razvstavanja[j]:
            if not je_i_dodan:
                kutije[i+1].append(razvstavanja[j][i])
                je_i_dodan = True

rjesenja = []
for k, v in kutije.items():
    for br in v:
        rjesenja.append([k, br])
        for i in range(len(v)):
            rjesenja.append([v[i], v[-1]])
            rjesenja.append([v[i-1], v[i]])

for i in range(q):
    if pitanja[i] in rjesenja:
        print("DA")

    else:
        print("NE")