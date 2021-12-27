for x in range(int(input())):
    n = int(input())
    cur_set = set()
    i = 1
    while i * i <= n:
        cur_set.add(i * i)
        i += 1
    i = 1
    while i * i * i <= n:
        cur_set.add(i * i * i)
        i += 1
    print(len(cur_set))
