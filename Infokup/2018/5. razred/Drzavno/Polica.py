broj_oznacenih_kamena = int(input())

kamenje = {}

for i in range(1, broj_oznacenih_kamena+1):
    kamenje[i] = int(input())

broj_preslagivanja = int(input())

preslagivanja = []
for i in range(broj_preslagivanja):
    preslagivanja.append(int(input()))

print(kamenje)
print(preslagivanja)

