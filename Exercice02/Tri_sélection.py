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

tri_selection([1,2,3,4,5,6,7,8,9,10])
tri_selection([10,9,8,7,6,5,4,3,2,1])

