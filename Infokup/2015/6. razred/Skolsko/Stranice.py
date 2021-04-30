# print(sum([len(str(i)) for i in range(1, int(input())+1)]))

num = int(input())

x = 0
counter = 0;

for i in range(1, num+1):
  x += len(str(i))
  if x >= num:
    counter = i
    break

print(counter)