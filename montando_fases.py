import heapq

mapa = {
    '1-1': [('1-2', 2), ('1-3', 4)],
    '1-2': [('1-1', 2), ('1-4', 7), ('1-3', 1)],
    '1-3': [('1-1', 4), ('1-2', 1), ('1-4', 3), ('Castelo', 5)],
    '1-4': [('1-2', 7), ('1-3', 3), ('Castelo', 2)],
    'Castelo': [('1-3', 5), ('1-4', 2)]
}

def prim(grafo, inicio):
    visitados = set()
    mst = []
    fila = []

    # Adiciona as arestas iniciais a partir do vértice de início
    visitados.add(inicio)
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila, (peso, inicio, vizinho))

    while fila:
        peso, origem, destino = heapq.heappop(fila)
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, peso))

            for prox_vizinho, prox_peso in grafo[destino]:
                if prox_vizinho not in visitados:
                    heapq.heappush(fila, (prox_peso, destino, prox_vizinho))

    return mst

# Executando o algoritmo a partir da fase '1-1'
if __name__ == "__main__":
    arvore_geradora = prim(mapa, '1-1')

    print("Mapa construído com as menores distâncias:\n")
    for origem, destino, peso in arvore_geradora:
        print(f"{origem} --({peso})--> {destino}")
