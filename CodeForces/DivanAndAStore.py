for i in range(int(input())):
    n, l, r, k = map(int, input().split())
    prices = sorted([int(x) for x in input().split()])
    num_of_chocolates = 0
    for j in range(n):
        if l <= prices[j] <= r and prices[j] <= k:
            num_of_chocolates += 1
            k -= prices[j]
    print(num_of_chocolates)
