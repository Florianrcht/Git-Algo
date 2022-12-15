import random

t = []

for i in range (10):
    ff = random.randint(0,100)
    t.append(ff)#Aleatoire
    #t.sort()#Meilleurs cas
    t.sort(reverse=True)#Pire cas

def tri_selection(t, comparaison, echange):
    nb = len(t)
    for i in range(0, nb):    
        minimum = i
        echange += 1
        for j in range(i + 1, nb) :
            comparaison += 1
            if t[j] < t[minimum] :
                minimum = j
                echange += 1
        if min is not i :
            temp = t[i]
            t[i] = t[minimum]
            t[minimum] = temp
            comparaison += 1
            echange += 3
    print(t, comparaison, echange)

comparaison = 0
echange = 0
tri_selection(t, comparaison, echange)
