prvi_krug = [int(i) for i in input().split()]
drugi_krug = [int(i) for i in input().split()]

kandidati = ["A", "B", "C", "D"]
for i in range(2): del kandidati[prvi_krug.index(min(prvi_krug))]
print(kandidati[drugi_krug.index(max(drugi_krug))])
