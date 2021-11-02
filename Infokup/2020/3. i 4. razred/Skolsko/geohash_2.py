n = int(input())
# polaz = int(input())
# kraj = int(input())

size = 2 ** n
geohash_tablica = [[0 for x in range(size)] for y in range(size)]
print(size)

for i in range(size):  # y
    iPom = i
    for j in range(size):  # x
        jPom = j
        test = ""
        print("---------")
        offset_one = size / 2
        offset_two = size / 2
        divider = size / 2
        divider_another = size / 2
        for x in range(n):
            print(offset_one)
            if jPom < offset_one:
                test += "0"
                offset_one /= 2
            else:
                test += "1"
                offset_one += divider
                divider /= 2
            if iPom < offset_two:
                test += "0"
                offset_two /= 2
            else:
                test += "1"
                offset_two += divider_another
                divider_another /= 2
            print(test)
            # if iPom > (2 ** n // 2):
            #     iPom /= 2  ##ovo promijeniti
            # if jPom > (2 ** n // 2):
            #     jPom /= 2  ##ovo promijeniti

            if (x + 1) == n:
                print(test)
                test2 = int(test, 2)
                geohash_tablica[i][j] = test2


for redak in geohash_tablica:
    print(*redak)
