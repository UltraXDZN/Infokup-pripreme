passengers = [[int(x) for x in input().split()] for i in range(int(input()))]

min_max_capacity = 0
cur_capacity = 0
for i in range(len(passengers)):
    cur_capacity = cur_capacity - passengers[i][0] + passengers[i][1]
    if cur_capacity > min_max_capacity:
        min_max_capacity = cur_capacity

print(min_max_capacity)