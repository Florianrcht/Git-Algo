def tri_insertion(tableau):
    compteur=0
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
            compteur=compteur+1
        #on insère l'élément à sa place
        tableau[j]=en_cours
        compteur=compteur+1
    print(tableau)
    print(compteur)
    

tableau1=[1,2,3,4,5,6,7,8,9,10]
tri_insertion(tableau1)


