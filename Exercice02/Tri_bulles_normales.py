Nmb = [17, 1, 28, 5]

for i in range(len(Nmb)-1, 0, -1):
  for j in range(0, i):
    if Nmb[j+1] < Nmb[j]:
      temp = Nmb[j+1]
      Nmb[j+1] = Nmb[j]
      Nmb[j] = temp

print(Nmb)