zbroj = 0
sdn = {
    2: 0,
    4: 0,
    3: 0,
    7: 0
}
while True:
    try:
        ssd, nums = input().split("|")
        ssd = ssd.split()
        nums = nums.split()
        for num in nums:
            try:
                sdn[len(num)] += 1
            except:
                continue
    except ValueError:
        break

for k, v in sdn.items():
    zbroj += v

print(zbroj)
