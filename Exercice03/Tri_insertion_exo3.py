import random

tableau1 = []

for i in range (10):
    ff = random.randint(0,100)
    tableau1.append(ff)#Aleatoire
    #tableau1.sort()#Meilleurs cas
    tableau1.sort(reverse=True)#Pire cas


def tri_insertion(tableau):
    comparaison = 0
    echange = 0
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        echange += 2

        comparaison+=2
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
            echange += 2
        tableau[j]=en_cours
        echange+=1

    print(tableau,comparaison, echange)


tri_insertion(tableau1)

