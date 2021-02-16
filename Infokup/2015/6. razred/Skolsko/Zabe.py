zabe = []

for i in range(4):
    zabe.append(int(input()))

if zabe[0] % 2 == 0:
    rjesenje = [zabe[3], zabe[0], zabe[1], zabe[2]]
else:
    rjesenje = [zabe[1], zabe[2], zabe[3], zabe[0]]

print(*rjesenje)