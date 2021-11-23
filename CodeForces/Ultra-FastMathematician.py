num_a = input()
num_b = input()
print("".join(["1" if num_a[i] != num_b[i] else "0" for i in range(len(num_a))]))