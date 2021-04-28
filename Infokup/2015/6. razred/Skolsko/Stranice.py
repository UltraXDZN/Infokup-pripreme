# print(sum([len(str(i)) for i in range(1, int(input())+1)]))

num = int(input())

counter = 0
i = 0
while i <= num:
    i += len(str(i))
    counter += 1

print(counter)
