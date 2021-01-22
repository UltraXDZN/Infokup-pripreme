dan = int(input())
vrijeme = int(input())

if dan > 1:
    print(dan + vrijeme)
elif dan == 1 and vrijeme == -1:
    print(31)
elif dan == 31 and vrijeme == 1:
    print(1)