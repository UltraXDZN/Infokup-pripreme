dimenzija_x, dimenzija_y = [int(dimenzija) for dimenzija in input().split()]

plocice = []
for i in range(dimenzija_x):
    plocice.append(input())

rjesenje = []
for i in range(1, dimenzija_x-1):
    for j in range(1, dimenzija_y-1):
        pronasao = False
        for m in range(1, dimenzija_x - 1):
            for n in range(1, dimenzija_y - 1):
                if plocice[i][j] != plocice[i % m][j % n]:
                    rjesenje.append(m)
                    rjesenje.append(n)
                    pronasao = True
                    break

print(*rjesenje)