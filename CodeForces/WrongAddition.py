for i in range(int(input())):
    a, s = input().split()
    a, s = a[::-1], s[::-1]
    b = ""

    while True:
        try:
            if int(s[0]) - int(a[0]) > -1:
                b += str(int(s[0]) - int(a[0]))
                s = s[1:]
            elif int(s[:2][::-1]) - int(a[0]) in range(10):
                b += str(int(s[:2][::-1]) - int(a[0]))
                s = s[2:]
            else:
                b = "0"
                break

            a = a[1:]
            if len(a) == 0:
                if len(s) > 0:
                    b += s[:]
                break
        except:
            b = "0"
            break

    print([-1, int(b[::-1])][b != "0"])
    # print("----------")
