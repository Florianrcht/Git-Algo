Nmb = [10,9,8,7,6,5,4,3,2,1]
longueur = len(Nmb)
interchangé = False
compteur=0
for i in range(longueur - 1):
    for j in range(0, longueur - i - 1):
        if Nmb[j] > Nmb[j + 1]:
            interchangé = True
            Nmb[j], Nmb[j + 1] = Nmb[j + 1], Nmb[j]
            compteur=compteur+1
    if not interchangé:
        break


print(Nmb)
print(compteur)
