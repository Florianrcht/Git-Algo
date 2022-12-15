import random

Nmb = []

for i in range (10):
    ff = random.randint(0,100)
    Nmb.append(i)


longueur = len(Nmb)
comparaison = 0
echange = 0

for i in range(len(Nmb)-1, 0, -1):
  for j in range(0, i):
      comparaison += 1
      if Nmb[j+1] < Nmb[j]:
          Nmb[j], Nmb[j + 1] = Nmb[j + 1], Nmb[j]
          echange += 3

print(Nmb, comparaison, echange)
