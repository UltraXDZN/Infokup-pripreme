for _ in range(int(input())):
    n, h, m = map(int, input().split())
    min_time = []
    ans = 12345
    for i in range(n):
        ah, am = map(int, input().split())
        x = h * 60 + m
        y = ah * 60 + am
        diff = y - x
        if diff < 0:
            diff += 1440
        ans = min(ans, diff)
    print(ans // 60, ans % 60)
