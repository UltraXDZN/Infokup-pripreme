broj_skinutih_mb = int(input())
rjesenje = ""

rjesenja = {
    0: "SKORO NISTA",
    25: "SKORO JEDNA CETVRTINA",
    50: "SKORO POLA",
    75: "SKORO TRI CETVRTINE",
    100: "SKORO SVE"
}

for k, v in rjesenja.items():
    if broj_skinutih_mb <= k:
        rjesenje = rjesenja[k]
        break

print(rjesenje)
