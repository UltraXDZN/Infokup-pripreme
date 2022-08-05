import sys


def check_aligment(n, l_a):
    # print(n, l_a)
    l_a_temp = list(set(l_a[:]))
    # print(l_a)
    if len(l_a_temp) != n:
        return False
    check_l = [False] * n
    for i in range(n):
        if (i + 1) == l_a_temp[i]:
            check_l[i] = True

    return [False, True][check_l.count(True) == n]



for _ in range(int(input())):
    input = sys.stdin.readline
    n = int(input())
    a = [int(x) for x in input().split()]
    # print(a)
    flag = check_aligment(n, a)
    if not flag and len(a) == n:
        i = 0
        while list(sorted(a)) != list(range(1, n + 1)):
            # print(a, a[i])
            if a[i] > n or a.count(a[i]) >= 2:
                a[i] //= 2
                if check_aligment(n, a):
                    flag = True
                    break
            i += 1
            if i == n:
                i = 0
            if all(x < n for x in a) and list(sorted(a)) != list(range(1, n + 1)) or a[i] == 0:
                break
    if check_aligment(n, a):
        flag = True
    # print(a)
    print(["NO", "YES"][flag])

