"""
Le but de cet exercice est de trier des tableaux en fonction de leur taille dans l'ordre croissant.
Cette taille est défini par une variable min, augmentera pas à pas grâce à la variable step et s'arrêtera quand elle aura atteint ou dépassera la variable max.
Le nombre de tableau est déterminé par la variable nbr, qui doit être aussi aléatoire.
"""

import random
import numpy
import statistics

t = []

def statSelection(mini: int, max: int, step: int, nbr: int):
    counter = 0
    for i in range(mini, max + 1, step):
        for j in range(1, nbr + 1, 1):
            m = numpy.random.randint(10, size=(i))
            nb = len(m)
            for k in range(0, nb):    
                minimum = k
                for l in range(k + 1, nb) :
                    if m[l] < m[minimum] :
                        minimum = l
                        counter = counter + 1
                if min is not k :
                    temp = m[k]
                    m[k] = m[minimum]
                    m[minimum] = temp
            t.append(counter)
            counter = 0
        mean = statistics.mean(t)
        print(i, mean)
        t.clear()

def statInsertion(mini: int, max: int, step: int, nbr: int):
    counter = 0
    for i in range(mini, max + 1, step):
        for j in range(1, nbr + 1, 1):
            m = numpy.random.randint(10, size=(i))
            for k in range(1,len(m)):
                en_cours = m[k]
                l = k
                while l>0 and m[l-1]>en_cours:
                    m[l]=m[l-1]
                    l = l-1
                    counter = counter + 1
                m[l]=en_cours
            t.append(counter)
            counter = 0
        mean = statistics.mean(t)
        print(i, mean)
        t.clear()

def statBullesNormales(mini: int, max: int, step: int, nbr: int):
    counter = 0
    for i in range(mini, max + 1, step):
        for j in range(1, nbr + 1, 1):
            m = numpy.random.randint(10, size=(i))
            for k in range(len(m)-1, 0, -1):
                for l in range(0, k):
                    if m[l+1] < m[l]:
                        temp = m[l+1]
                        m[l+1] = m[l]
                        m[l] = temp
                        counter = counter + 1
            t.append(counter)
            counter = 0
        mean = statistics.mean(t)
        print(i, mean)
        t.clear()

def statBullesOptimisees(mini: int, max: int, step: int, nbr: int):
    counter = 0
    for i in range(mini, max + 1, step):
        for j in range(1, nbr + 1, 1):
            m = numpy.random.randint(10, size=(i))
            longueur = len(m)
            interchangé = False
            for k in range(longueur - 1):
                for l in range(0, longueur - k - 1):
                    if m[l] > m[l + 1]:
                        interchangé = True
                        m[l], m[l + 1] = m[l + 1], m[l]
                        counter = counter + 1
                if not interchangé:
                    break
            t.append(counter)
            counter = 0
        mean = statistics.mean(t)
        print(i, mean)
        t.clear()
