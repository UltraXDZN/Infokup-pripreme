def find_collumn(b1, b2):
    for x in range(len(board[0])):
        if [row[x] for row in b1] == [row[x] for row in b2]:
            return True


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

i = 5
has_found_bingo = False
is_column = False
fn = 0
board_num = 0
board_lucky = []
while not has_found_bingo:
    lucky = luckyNums[:i - 1]
    i += 1
    for board in boards:
        board_lucky = []
        for row in board:
            row_lucky = [0] * 5
            for num in lucky:
                fn = num
                if num in row:
                    row_lucky[row.index(num)] = num
                if row_lucky == row or find_collumn(board, board_lucky):
                    has_found_bingo = True
                    board_num = boards.index(board)
                    break
            board_lucky.append(row_lucky)
        has_found_bingo = [has_found_bingo, find_collumn(board, board_lucky)][not has_found_bingo]
        if has_found_bingo:
            if len(boards) > 1:
                boards.remove(board)
                has_found_bingo = False
                continue
            break

board_sum = 0
for row in boards[board_num]:
    for num in row:
        if num not in board_lucky[board.index(row)]:
            board_sum += num

print(fn * board_sum)
