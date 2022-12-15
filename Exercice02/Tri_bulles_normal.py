Nmb = [10,9,8,7,6,5,4,3,2,1]
compteur=0
for i in range(len(Nmb)-1, 0, -1):
  for j in range(0, i):
    if Nmb[j+1] < Nmb[j]:
      temp = Nmb[j+1]
      Nmb[j+1] = Nmb[j]
      Nmb[j] = temp
      compteur=compteur+1

print(Nmb)
print(compteur)
