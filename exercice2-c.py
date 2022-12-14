"""
Algorithme tri par insertion:

 debut algorithme de la methode de  tri par insertion (params:tableau)
        i est egale a 1
        tant que i est egale ou inferieur à longueur de la tableau - 1

            # mémoriser tableau[i] dans x
            x sauvegarde la valeur de tableau[i]                            

            # décaler les éléments tableau[0]..tableau[i-1] qui sont plus grands que x, en partant de tableau[i-1]
            j prend la valeur de i                               
            tant que j est superieur à 0 et tableau[j - 1] supérieur à x
                    tableau[j] prend la valeur de  tableau[j - 1]
                    j prend la valeur de j - 1
                    fin de tant que
            # placer x dans l'espace laissé par le décalage
            tableau[j] prend la valeur de x    
"""
def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        #on insère l'élément à sa place
        tableau[j]=en_cours
    print(tableau)
tableau1=[8,4,0,3]
tri_insertion(tableau1)


