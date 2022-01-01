def replace_bool(list_a, index, p_list): list_a[p_list[index]] = True; return list_a


def solve():
    n = int(input())
    main = [int(x) for x in input().split()]
    a, bigger = [False] * (n + 1), []
    [replace_bool(a, i, main) if main[i] <= n and a[main[i]] is False else bigger.append(main[i]) for i in range(n)]
    bigger = sorted(bigger)
    counter = 0
    for i in range(1, n + 1):
        if not a[i]:
            if ((bigger[counter] - 1) // 2) >= i:
                counter += 1
            else:
                return -1
    return counter


try:
    print(*[solve() for _ in range(int(input()))], sep="\n")
except Exception as error:
    print(error)
