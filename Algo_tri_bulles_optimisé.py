Nmb = [84, 34, 25, 12, 22, 11, 90]
longueur = len(Nmb)
interchangé = False
for i in range(longueur - 1):
    for j in range(0, longueur - i - 1):
        if Nmb[j] > Nmb[j + 1]:
            interchangé = True
            Nmb[j], Nmb[j + 1] = Nmb[j + 1], Nmb[j]
    if not interchangé:
        break


print(Nmb)