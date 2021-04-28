# print(sum([len(str(i)) for i in range(1, int(input())+1)]))

num = int(input())

counter = 0
i = 1
while i <= num:
    counter += 1
    i += len(str(i))

print(counter)