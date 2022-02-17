for _ in range(int(input())):
    n, k = map(int, input().split())
    s = set([int(x) for x in input().split()])

    if k:
        mex_num = 0
        while mex_num in s:
            mex_num += 1

        max_num = max(s)
        num_to_add = (max_num + mex_num + 1) // 2

        if num_to_add != mex_num:
            s.add(num_to_add)
            k = 0
    print(len(s) + k)
