def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            print(a, i, a / i)
            return False

    return True


n, e = map(int, input().split())
contents = [int(x) for x in input().split()]

for i in range(1, len(contents) - 1):
    print(i)
    for k in range(1, i + 1):
        print(i, k, i + 1 + k * e)
        if 1 <= i and 1 <= k:
            print("STEP 1")
            if (i + e * k) <= n:
                print("STEP 2")
                if is_prime(contents[i] * contents[i + 1 + k * e]):
                    print(contents[i] * contents[i + e])
                    print("success")
                    print()
