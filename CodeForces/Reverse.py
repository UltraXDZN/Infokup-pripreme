x, y = map(int, input().split())
x_bin, y_bin = bin(x)[2:], bin(y)[2:]
if x_bin == y_bin:
    print('YES')
elif y_bin[-1] == '0':
    print('NO')
else:
    x_bin += '1'
    if (y_bin.find(x_bin) != -1 or y_bin.find(x_bin[::-1]) != -1) and y_bin.count('1') - x_bin.count('1') == len(
            y_bin) - len(x_bin):
        print('YES')
    else:
        x_bin = x_bin[:-1]
        while x_bin[-1] == '0':
            x_bin = x_bin[:-1]
        print('YES') if (y_bin.find(x_bin) != -1 or y_bin.find(x_bin[::-1]) != -1) and y_bin.count('1') - x_bin.count(
            '1') == len(y_bin) - len(x_bin) else print('NO')
