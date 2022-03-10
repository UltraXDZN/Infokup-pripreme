for _ in range(int(input())):

    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    a.sort()
    b.sort()

    k = n // 4
    a_s = sum(a[k:])
    b_s = sum(b[k:])

    ans = 0
    j = k - 1
    while b_s > a_s:
        n += 1
        a_s += 100
        if n % 4 == 0:
            a_s -= a[k]
            k += 1
        else:
            if j >= 0:
                b_s += b[j]
                j -= 1

        ans += 1
    print(ans)
