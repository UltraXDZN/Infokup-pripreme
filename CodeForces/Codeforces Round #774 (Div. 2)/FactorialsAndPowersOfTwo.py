def factorials(n):
    factorials_list = []
    prod = 6
    i = 4
    while prod <= n:
        factorials_list.append(prod)
        prod *= i
        i += 1
    return factorials_list


def count(a):
    ans = 9223372036854775807  # sys.maxSize
    for mask in range(1 << len(a)):
        s = n
        for i in range(len(a)):
            s -= [0, a[i]][mask & (1 << i) != 0]
            # check if mask (cur value of the loop) bitwise and-ed with leftwise i by 1 is different than zero
        if s < 0:
            continue
        ans = min(bin(mask).count("1") + bin(s).count("1"), ans)
    return ans


for _ in range(int(input())):
    n = int(input())
    a = factorials(n)  # generate all factorials
    print(count(a))
