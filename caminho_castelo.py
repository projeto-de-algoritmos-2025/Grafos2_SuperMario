import json
import heapq

def Dijkstra(mapa, origem, destino):
    fila = [(0, origem, [])]  
    visitados = set()

    while fila:
        custo, atual, caminho = heapq.heappop(fila)

        if atual in visitados:
            continue
        visitados.add(atual)

        caminho = caminho + [atual]

        if atual == destino:
            return custo, caminho  # caminho encontrado

        for vizinho, peso in mapa.get(atual, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, caminho))

    return float('inf'), []  # se não houver caminho

def carregar_mapa_do_jogo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados['mapa'], dados['origem'], dados['destino']

if __name__ == "__main__":
    mapa, origem, destino = carregar_mapa_do_jogo('mapa_mario.json')
    custo_total, caminho_otimo = Dijkstra(mapa, origem, destino)

    if caminho_otimo:
        print(f"\n🏁 Caminho mais fácil do Mario até o castelo:")
        print(" -> ".join(caminho_otimo))
        print(f"Custo total da jornada: {custo_total}")
    else:
        print("❌ Não foi possível encontrar um caminho até o castelo.")
