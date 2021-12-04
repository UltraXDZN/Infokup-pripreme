n = input()
print(["NO", "YES"][n.__contains__("1111111") or n.__contains__("0000000")])