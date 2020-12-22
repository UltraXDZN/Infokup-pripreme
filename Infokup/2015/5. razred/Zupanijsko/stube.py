ulaz = int(input())
br_stuba = [1, 2, 3]
brojac = 0
#rjesenje = ulaz // 3 * 6 + br_stuba[ulaz % 3]
for i in range(ulaz):
    brojac += br_stuba[i % 3]
print(brojac)
