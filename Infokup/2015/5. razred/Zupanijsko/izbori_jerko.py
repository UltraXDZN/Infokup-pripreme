prvi_krug = [int(i) for i in input().split()]
drugi_krug = [int(i) for i in input().split()]

kandidati = ["A", "B", "C", "D"]

del kandidati[prvi_krug.index(min(prvi_krug))]
del kandidati[prvi_krug.index(min(prvi_krug))]
print(kandidati[drugi_krug.index(max(drugi_krug))])
