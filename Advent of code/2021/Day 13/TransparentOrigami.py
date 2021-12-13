def print_list(arr):
    for row in arr:
        print(*row, sep="")


x_ins = []
y_ins = []
while True:
    try:
        j, y = map(int, input().split(","))
        x_ins.append(j)
        y_ins.append(y)
    except ValueError:
        break

type_f = ""
fold = input()
if "x=" in fold:
    type_f = "X"
    fold = int(fold.replace("fold along x=", ""))
elif "y=" in fold:
    type_f = "Y"
    fold = int(fold.replace("fold along y=", ""))

print(fold)
print(len(x_ins) + len(y_ins))
table = [["." for j in range(max(x_ins) + 1)] for i in range(max(y_ins) + 1)]

for i in range(len(x_ins)):
    for y in range(y_ins[i] + 1):
        for j in range(x_ins[i] + 1):
            if y == y_ins[i] and j == x_ins[i]:
                table[y][j] = "#"

# print(table)
table_final = table

# for i in range(len(fold_y)):
if type_f == "Y":
    print("Y")
    table.insert(fold, ["-"] * int(len(x_ins) / 2 + 2))
    table_final = table[:fold]
    table_2 = table[fold + 1:]
    for i in range(len(table_final)):
        for j in range(len(table_final[i])):
            if table_final[i][j] == "." and table_2[-(i + 1)][j] == "#":
                table_final[i][j] = "#"
    table = table_final


else:
    print("X")
    print(fold)
    for i in range(len(table)):
        table[i][fold] = "|"

    table_final = []
    table_2 = []

    is_reversed_left = [False, True][max(x_ins) + 1 - fold > (max(x_ins) + 1) // 2]
    val = abs((len(table[0]) - fold) - (len(table[0])) // 2)
    print(val)
    for i in range(len(table)):
        table_final.append([table[i][:fold], ["."] * abs(val) + table[i][:fold]][not is_reversed_left])
        table_2.append([["."] * abs(val) + table[i][:fold], table[i][fold + 1:][::-1]][is_reversed_left])
        # print(table_1[i], table_2[i])

    for i in range(len(table_final)):
        for j in range(len(table_final[i])):
            if table_final[i][j] == "." and table_2[i][j] == "#":
                table_final[i][j] = "#"
    # table = table_1

count_hashes = 0
for i in range(len(table_final)):
    for j in range(len(table_final[i])):
        count_hashes += [0, 1][table_final[i][j] == "#"]

print()
print_list(table_final)
print(count_hashes)
