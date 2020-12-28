broj_test_podataka = int(input())
bodovi_po_testu = int(input())
osvojeni_bodovi = int(input())

print("DA" if osvojeni_bodovi % bodovi_po_testu == 0 and osvojeni_bodovi / bodovi_po_testu <= broj_test_podataka else "NE")