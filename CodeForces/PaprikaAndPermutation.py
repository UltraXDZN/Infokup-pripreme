def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    counter = 0
    final = set()
    for i in range(n):
        if a[i] == (i + 1) or a[i] == n and a[i] not in final:
            final.add(a[i])
            continue
        x = abs(a[i] - [i, i + 1][a[i] == (a[i] - i)])
        if (a[i] % x) == [i, i + 1][a[i] == (a[i] - i)]:
            final.add(a[i] % x)
            counter += 1
        elif (i + 1) > a[i]:
            continue
        else:
            return -1
    return counter


print(*[solve() for _ in range(int(input()))], sep="\n")
