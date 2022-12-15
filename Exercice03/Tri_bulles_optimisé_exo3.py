import random

Nmb = []

for i in range (10):
    ff = random.randint(0,100)
    Nmb.append(ff)#Aleatoire
    #Nmb.sort()#Meilleurs cas
    Nmb.sort(reverse=True)#Pire cas


longueur = len(Nmb)
comparaison = 0
echange = 0
interchangé = False

for i in range(longueur - 1):
    for j in range(0, longueur - i - 1):
        comparaison += 1
        if Nmb[j] > Nmb[j + 1]:
            interchangé = True
            Nmb[j], Nmb[j + 1] = Nmb[j + 1], Nmb[j]
            echange += 3
    if not interchangé:
        break


print(Nmb, comparaison, echange)


