for _ in range(int(input())):
    n, k = map(int, input().split())
    if k <= int(n / 2 + 0.9):
        chessboard = [["."] * n for _ in range(n)]
        for i in range(k):
            chessboard[i * 2][i * 2] = "R"
        print(*["".join(x) for x in chessboard], sep="\n")
    else:
        print(-1)