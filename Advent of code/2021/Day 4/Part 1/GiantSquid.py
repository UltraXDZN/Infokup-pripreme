luckyNums = [int(x) for x in input().split(",")]

boards = []
while True:
    board = []
    for i in range(6):
        row = []
        for j in input().split():
            row.append(int(j))
        board.append(row)
    boards.append(list(board[1::]))
    if not board[-1]:
        boards.remove(boards[-1])
        break

j = 0
i = 5
has_found_bingo = False
is_column = False
fn = 0
board_num = 0
board_lucky = []
while not has_found_bingo:
    lucky = luckyNums[:i + j]
    i += 1
    j = i
    for board in boards:
        board_lucky = []
        for row in board:
            row_lucky = [0] * 5
            for num in lucky:
                if num in row:
                    row_lucky[row.index(num)] = num
                if row_lucky == row:
                    fn = num
                    has_found_bingo = True
                    board_num = boards.index(board)
            board_lucky.append(row_lucky)
        for x in range(len(board[0])):
            if [row[x] for row in board] == [row[x] for row in board_lucky]:
                has_found_bingo = True

        if has_found_bingo:
            break

board_sum = 0
for row in boards[board_num]:
    for num in row:
        if num not in board_lucky[board.index(row)]:
            board_sum += num

print(fn * board_sum)
