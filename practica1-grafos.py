import random

cola = []
visitados = []
nodo_raiz = 21
solucion = random.randint(0, 24)
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

print(f"Nodo a buscar: {solucion}")
print(f"Nodo raíz: {nodo_raiz}")

cola.append(nodo_raiz)
for nodo in cola:
    if nodo == solucion:
        print(f"Objetivo alcanzado: {nodo}")
        break
    else: 
        if nodo not in visitados:
            visitados.append(nodo)
            for conexion in grafo[nodo]:
                if conexion not in visitados and conexion not in cola:
                    cola.append(conexion)
        print(f"Cola de espera{cola}")
        print(f"Historial de visitados: {visitados}\n")

Ya funciona como debe
