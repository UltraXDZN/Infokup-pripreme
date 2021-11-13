n, m, q = map(int, input().split())

kutije = [[]] * n

razvstavanja = []
for i in range(m):
    razvstavanja.append([int(x) for x in input().split()])

pitanja = []
for i in range(q):
    pitanja.append([int(x) for x in input().split()])

rjesenja = []
for i in range(n):
    for j in range(n):
        rjesenja.append([i, j])
        rjesenja.append([j, i])

for i in range(n):
    for j in range(m):
        je_i_dodan = False
        for num in razvstavanja[j]:
            if not je_i_dodan:
                kutije[i].append(razvstavanja[j][i])
                je_i_dodan = True
#
# rjesenja = []
# for brojevi in kutije:
#     for br in brojevi:
#         rjesenja.append([brojevi.index(br), br])
#         for i in range(len(brojevi)):
#             if [brojevi[i], brojevi[-1]] not in rjesenja:
#                 rjesenja.append([brojevi[i], brojevi[-1]])
#             if [brojevi[i-1], brojevi[i]] not in rjesenja:
#                 rjesenja.append([brojevi[i-1], brojevi[i]])
#
# print(rjesenja)

for i in range(q):
    if pitanja[i] in rjesenja:
        print("DA")
    else:
        print("NE")