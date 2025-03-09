def wJugDFS(c1, c2, g):
    s= [(0, 0)]
    v= set()
    v.add((0, 0))
    a = []

    while s:
        j1, j2= s.pop()
        a.append((j1, j2))
    
        if j1== g or j2== g:
            print("Solution Found")
            for act in a:
                print(act)
            return 

        r= [(c1, j2),
            (j1, c2),
            (0, j2),
            (j1, 0),
            (j1 - min(j1, c2 - j2), j2 + min(j1, c2 - j2)),
            (j1 + min(j2, c1 - j1), j2 - min(j2, c1 - j1)),
            (min(j1 + j2, c1), 0),
            (0, min(j1 + j2, c2))]

        for state in r:
            if state not in v:
                v.add(state)
                s.append(state)

    print("No Solution found")
    return 

jug1Cap= int(input("Enter the capacity of jug 1: "))
jug2Cap= int(input("Enter the capacity of jug 2: "))
target= int(input("Enter the target amount: "))

wJugDFS(jug1Cap, jug2Cap, target)
