def solve(x, y):
    if x is y:
        rj[x, y] = x
        return
    else:
        for j in range(x, y+1):
            if j == x:
                # print(j+1, y)
                if (j + 1, y) in s and s[j + 1, y]:
                    rj[x, y] = j
                    solve(x + 1, y)
                    break
            elif j == y:
                if (x, j - 1) in s and s[x, j - 1]:
                    rj[x, y] = j
                    solve(x, j - 1)
                    break
            else:
                if (x, j - 1) in s and s[x, j - 1] and (j + 1, y) in s and s[j + 1, y]:
                    rj[x, y] = i
                    solve(x + 1, y)
                    solve(x, j - 1)
                    break


for _ in range(int(input())):
    s, rj = {}, {}
    n = int(input())
    for i in range(n):
        l, r = map(int, input().split())
        s[l, r] = True
    solve(1, n)
    for k, v in rj.items():
        print(*k, v)
    print()