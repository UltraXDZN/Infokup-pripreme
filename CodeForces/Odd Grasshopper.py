for _ in range(int(input())):
    x0, jmp = map(int, input().split())
    print(x0 + [-1, 1][x0 % 2 == 0] * [0, -jmp, 1, jmp + 1][jmp % 4])
