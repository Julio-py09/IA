cola = []
visitados = []
nodo = 0
solucion = 4
grafo={
    0:[1,2],
    1:[0,3,4],
    2:[0,5,6],
    3:[1,7,8],
    4:[1,9,10],
    5:[2,11,12],
    6:[2,13,14],
    7:[3,15,16],
    8:[3,17,18],
    9:[4,19],
    10:[4,20],
    11:[5,21],
    12:[5,22],
    13:[6,23],
    14:[6,24],
    15:[7],
    16:[7],
    17:[8],
    18:[8],
    19:[9],
    20:[10],
    21:[11],
    22:[12],
    23:[13],
    24:[14]
}

cola = [0]
while len(cola) > 0:
    nodo = cola.pop()
    if nodo == solucion:
        print(nodo)
        break
    else:
        visitados.append(nodo)
        for hijos_grafo in grafo[nodo]:
            if hijos_grafo not in visitados:
                visitados.append(hijos_grafo)
                cola.append(hijos_grafo)