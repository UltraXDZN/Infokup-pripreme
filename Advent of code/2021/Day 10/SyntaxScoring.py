def find_count_simbol_in_line(line, s, es):
    new_line = line
    while s[0] in new_line or s[1] in new_line or s[2] in new_line or s[3] in new_line:
        for i in range(len(s)):
            new_line = new_line.replace(s[i], "")

    for i in range(len(new_line) - 1):
        if f"{new_line[i]}{new_line[i + 1]}" in es:
            return new_line[i + 1]

    return new_line


points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
chars = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

symbols = ["()", "[]", "{}", "<>"]
error_symbols = []
for i in range(len(symbols)):
    for j in range(len(symbols)):
        cur_str = f"{symbols[i][0]}{symbols[j][1]}"
        if cur_str not in symbols:
            error_symbols.append(cur_str)

sum_of_all = 0
sums_to_add = []

while True:
    syntax_in = input()
    if syntax_in:
        symbol = find_count_simbol_in_line(syntax_in, symbols, error_symbols)[::-1]
        if len(symbol) == 1:  # part 1
            sum_of_all += points[symbol]
        else:  # part 2
            new_sum = 0
            for i in range(len(symbol)):
                new_sum = 5 * new_sum + chars[symbol[i]]
            sums_to_add.append(new_sum)
    else:
        break

print(sum_of_all)
print(sorted(sums_to_add)[int(len(sums_to_add) / 2)])