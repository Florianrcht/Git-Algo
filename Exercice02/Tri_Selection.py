def tri_selection(t):
    nb = len(t)
    for i in range(0, nb):    
        minimum = i
        for j in range(i + 1, nb) :
            if t[j] < t[minimum] :
                minimum = j
        if min is not i :
            temp = t[i]
            t[i] = t[minimum]
            t[minimum] = temp
    print(t)

tri_selection([2, 3, 8, 5, 4, 25, 72, 17, 729])