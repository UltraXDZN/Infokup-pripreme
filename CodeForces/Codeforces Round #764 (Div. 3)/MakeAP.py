def check_progression(l_a):
    return [False, True][(l_a[2] - l_a[1]) == (l_a[1] - l_a[0])
                         or l_a[0] == l_a[1] == l_a[2]
                         or ((l_a[1] * 2) - l_a[2]) % l_a[0] == 0 and ((l_a[1] * 2) - l_a[2]) > 0
                         or ((l_a[1] * 2) - l_a[0]) % l_a[2] == 0 and ((l_a[1] * 2) - l_a[0]) > 0
                         or (l_a[0] + l_a[2]) % (2 * l_a[1]) == 0]


for i in range(int(input())):
    a = [int(x) for x in input().split()]
    print(["NO", "YES"][check_progression(a)])
