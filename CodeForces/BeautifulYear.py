year = str(int(input()) + 1)

is_distinct = False
while not is_distinct:
    counts = []
    for num in year:
        counts.append(year.count(num))

    if max(counts) == 1:
        is_distinct = True
        break
    year = str(int(year) + 1)

print(year)
