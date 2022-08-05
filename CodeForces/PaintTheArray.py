def solve(list_a, gcd_val1, gcd_val2):
    for i in range(1, len(list_a), 2):
        if list_a[i] % gcd_val1 == 0:
            return gcd_val1

    for i in range(0, len(list_a), 2):
        if list_a[i] % gcd_val2 == 0:
            return gcd_val2
    return 0


gcd = lambda a, b: b if a == 0 else gcd(a % b, a)
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    color_1_gcd, color_2_gcd = a[0], a[1]
    for i in range(1, n):
        if i % 2 != 0:
            color_2_gcd = gcd(color_2_gcd, a[i])
            continue
        color_1_gcd = gcd(color_1_gcd, a[i])
    print(solve(a, color_1_gcd, color_2_gcd))
