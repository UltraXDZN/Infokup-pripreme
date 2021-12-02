n = int(input())
cards = [int(i) for i in input().split()]
sd = [0, 0]
i = 0
while cards:
    sd[i] += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
    i ^= 1

print(*sd)
