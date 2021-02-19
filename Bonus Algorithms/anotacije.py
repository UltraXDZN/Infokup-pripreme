items = [
    # 20 / 1,25 = 16  # osnovica
    # 20 - 16 = 4kn  # iznos poreza
    {
        'proizvod': 'Napolitanke',
        'cijena': 20.00,
        'stopa_poreza': 'PDV 25%'
    },
    {
        'proizvod': 'kruh bijeli',
        'cijena': 8.00,
        'stopa_poreza': 'PDV 0%'
    },
    {
        'proizvod': 'mlijeko 1l',
        'cijena': 5.50,
        'stopa_poreza': 'PDV 5%'
    },
    {
        'proizvod': 'Čips',
        'cijena': 7.00,
        'stopa_poreza': 'PDV 25%'
    },
    {
        'proizvod': 'toaletni papir',
        'cijena': 15.00,
        'stopa_poreza': 'PDV 25%'
    },
    {
        'proizvod': 'kajzerica',
        'cijena': 2.00,
        'stopa_poreza': 'PDV 0%'
    },
    {
        'proizvod': 'jogurt',
        'cijena': 3.00,
        'stopa_poreza': 'PDV 5%'
    },

]

# izračunati po stopama:
# 1. ukupno cijena po stopama
# 2. koliko iznosi porez po svakoj stopi
# ukupno cijena: 123.45kn

####
# stopa: PDV 25%, ukupno: 45.45kn, iznos poreza: 9.75kn, osnovica: 33,60kn
# stopa: PDV 5%, ukupno: 24.36kn, iznos poreza: 4.95kn
# stopa: PDV 0%, ukupno: 34.74kn, iznos poreza: 8.58kn

def pronadji_porez(pdv):
    pdv = pdv.replace("PDV ", "")
    pdv = pdv.replace("%", "")
    return pdv if len(pdv) > 1 else f"0{pdv}"

stope = {
    'PDV 25%': [],
    'PDV 5%': [],
    'PDV 0%': []
}

for item in items:
    stope[item['stopa_poreza']].append(item['cijena'])

# print(stope)


for porez in stope:
    ukupna_cijena = sum(stope[porez])
    ukupna_cijena_poreza = 0
    pdv = pronadji_porez(porez)
    temp_uk = ukupna_cijena
    ukupna_cijena = ukupna_cijena / float(f'1.{pdv}') #if float(f'0.{pdv}') > 0 else 0
    ukupna_cijena_poreza = temp_uk - ukupna_cijena
    iznos_poreza = format(ukupna_cijena_poreza, '.2f')
    ukupno = format(ukupna_cijena, '.2f')

    print(f"stopa: {porez}, ukupno: {ukupno}kn, iznos poreza: {iznos_poreza}kn")


# print(stope)
