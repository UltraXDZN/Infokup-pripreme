for _ in range(int(input())):
    s = input()
    c = input()
    found = False
    for i in range(len(s)):
        if c == s[i]:
            left = i
            right = len(s) - (i + 1)
            if left % 2 == 0 and right % 2 == 0:
                found = True

    print(["NO", "YES"][found])
