num = int(input())
a = b = num // 2
if a % 2 != 0 and b % 2 != 0:
    if a - 1 != 0 or b - 1 != 0:
        if a >= b:
            b += 1
            a -= 1
        else:
            a += 1
            b -= 1

if a % 2 == 0 and b % 2 == 0 and a + b == num:
    print("YES")
else:
    print("NO")
