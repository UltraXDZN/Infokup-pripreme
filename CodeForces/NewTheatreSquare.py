for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    a = [input() for i in range(n)]
    ct = 0
    for i in range(n):
        ct_x, ct_y = 0, 0
        vis = [0] * m
        for j in range(m):
            if j + 1 < m and a[i][j + 1] == a[i][j] == "." and not vis[j]:
                ct_y += y
                vis[j], vis[j + 1] = 1, 1
            if a[i][j] == ".":
                ct_x += x
                if not vis[j]:
                    ct_y += x
        ct += [ct_x or ct_y, min(ct_y, ct_x)][ct_x > 0 and ct_y > 0]

    print(ct)
