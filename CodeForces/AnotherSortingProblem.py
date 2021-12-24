n, m = map(int, input().split())
letters = [0] * n

for i in range(n):
    a = input()
    cur = 0
    change = True
    for j in range(m):
        cur = cur * 26 + change * ord(a[j])
        change *= -1
    letters[i] = [cur, i]

print(*[sum([letter[1], 1]) for letter in sorted(letters)])
