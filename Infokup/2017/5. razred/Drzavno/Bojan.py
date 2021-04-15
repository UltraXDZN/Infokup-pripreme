from typing import List

broj_stupaca = int(input())
stupci = [int(i) for i in input().split()]
broj_bojanja_zida = int(input())
koraci = []
for i in range(broj_bojanja_zida):
    koraci.append([int(i) for i in input().split()])

for korak in koraci:
    print()
    for i in range(korak[0]-1, korak[1]):
        print(stupci[i], end=" ")