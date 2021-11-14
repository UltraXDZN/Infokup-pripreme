n, k = map(int, input().split())
contestants = [int(x) for x in input().split()]

passing = 0
for i in range(0, n):
    if i >= k and contestants[i - 1] != contestants[k]:
        break
    if (i <= k or contestants[i - 1] == contestants[i] and contestants[i] == contestants[k]) and contestants[i] != 0:
        passing += 1

print(passing)
