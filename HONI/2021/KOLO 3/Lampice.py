n, k = map(int, input().split())
pattern = [str(x) for x in input().split()]


def pattern_finder(mylist, pattern):
    matches = []
    i = 0
    while i < len(mylist):
        if mylist[i] == pattern[0] and mylist[i:i + len(pattern)] == pattern:
            matches.append(i)
            i += len(pattern)
        else:
            i += 1
    return matches


def get_patterns(list_input, p=None):
    if type(list_input[0]) != list:
        list_input = [list_input]
    result = []
    for list_in in list_input:
        if len(set(list_in)) == 1:
            result.append([1, list_in])
            continue
        n = len(list_in)
        if n == 1:
            result.append(list_in[0])
            continue
        p_len = p
        if p is None:
            p_len = int(n / 2)
        lhs = 0
        rhs = lhs + p_len
        list_split = list_in
        if p_len <= 1:
            result.append([1, list_in])
            continue
        found = False
        while lhs < n - p_len and not found:
            rhs = lhs + p_len
            while rhs <= n - p_len:
                if list_in[lhs:lhs + p_len] == list_in[rhs:rhs + p_len]:
                    found = True
                    matches = pattern_finder(list_in, list_in[lhs:lhs + p_len])
                    list_split = []

                    for i, m in enumerate(matches):
                        if i == 0 and m != 0:
                            list_split.append(list_in[0:m])
                            continue
                        if i == len(matches) - 1:
                            if m + p_len != n:
                                list_split.append(list_in[m + p_len:])
                            continue
                        if m + p_len != matches[i + 1]:
                            list_split.append(list_in[m + p_len:matches[i + 1]])
                    result.append([len(matches), list_in[lhs:lhs + p_len]])
                    break
                rhs += 1
            lhs += 1
        if not list_split:
            continue
        if not found:
            result += get_patterns(list_split, p_len - 1)
        else:
            result += get_patterns(list_split)
    return result


patterns = get_patterns(pattern)
print(pattern)
print(patterns)

has_found = False
if len(patterns) == 1 or len(patterns[0][1]) == 1:
    print(1)
    print(*patterns[0][1])
    has_found = True

for i in range(len(patterns)):
    if not has_found:
        new_list = set(patterns[i][1])
        for p in new_list:
            if "".join([p] * k) in "".join(patterns[i][1]) and "".join(patterns[i][1]).count("".join(p)) > 1:
                list_w_a = [p] * k
                list_w_a = list(dict.fromkeys(list_w_a))
                if len(list_w_a) > 1:
                    print(len(list_w_a))
                    print(*list_w_a)
                    has_found = True
                    break

        if patterns[i][0] != 1 or len(patterns) == 1:
            patterns[i][1] = list(dict.fromkeys(patterns[i][1]))
            if "".join(patterns[i][1] * 2) in "".join(pattern):
                print(len(patterns[i][1]))
                print(*patterns[i][1])
                has_found = True
                break

if not has_found:
    print(-1)

# patrn = list(dict.fromkeys(pattern))
# print(*pattern)
# print(uzorak)
