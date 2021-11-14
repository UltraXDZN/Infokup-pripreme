num_of_op = int(input())
x = 0
for i in range(num_of_op):
    operation = input()
    if operation.count("+") >= 1:
        x += 1
    elif operation.count("-") >= 1:
        x -= 1

print(x)