Nmb = [17, 1, 28, 5]

for i in range(len(Nmb)-1, 0, -1):
  for step in range(0, i):
    if Nmb[step+1] < Nmb[step]:
      conteneur = Nmb[step+1]
      Nmb[step+1] = Nmb[step]
      Nmb[step] = conteneur

print(Nmb)