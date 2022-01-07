import sys
input = sys.stdin.readline
inf = 11e9

for _ in range(int(input())):
    max_size = 0
    max_size_cost = 0
    leftmost, rightmost = inf, 0
    l_cost, r_cost = 0, 0
    for i in range(int(input())):
        l, r, cost = map(int, input().split())
        if (r - l + 1) > max_size or ((r - l + 1) == max_size and max_size_cost > cost):
            max_size_cost = cost
            max_size = r - l + 1

        if l < leftmost or (l == leftmost and cost < l_cost):
            l_cost = cost
            leftmost = l

        if r > rightmost or (r == rightmost and cost < r_cost):
            r_cost = cost
            rightmost = r

        # print(f"R: {r_cost, rightmost} L: {l_cost, leftmost} C: {cost, max_size_cost, max_size}")
        print([r_cost + l_cost,
               min(max_size_cost, r_cost + l_cost)][(rightmost - leftmost + 1) == max_size])
