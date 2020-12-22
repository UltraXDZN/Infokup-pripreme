mladi_mj = int(input())
prva_cet_mj = int(input())
puni_mj = int(input())
druga_cet_mj = int(input())

trenutni_mj = int(input())

if mladi_mj <= trenutni_mj and trenutni_mj < prva_cet_mj:
    print("MLADI")
elif prva_cet_mj <= trenutni_mj and trenutni_mj < puni_mj:
    print("PRVA")
elif puni_mj <= trenutni_mj and trenutni_mj < druga_cet_mj:
    print("PUNI")
elif druga_cet_mj <= trenutni_mj:
    print("ZADNJA")