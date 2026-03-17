import heapq

def h()->dict[int,float]:
    h={}
    with open("dist-euclidiana.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        for l in lines:
            if l != "ID h(n)":
                l = l.split()
                h[int(l[0])]=float(l[1])
    return h

def g():
    grafo = {}
    with open("conexoes.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        for l in lines:
            if l != "Origem Destino Custo":
                l = l.split()
                origem = int(l[0])
                destino = int(l[1])
                peso = float(l[2])
                
                if origem not in grafo:
                    grafo[origem] = {}

                grafo[origem][destino] = peso
    return grafo

def astar(grafo, heuristicas, inicio, objetivo):
    fila = []
    heapq.heappush(fila, (0, inicio)) # Cria fila de prioridade f(n) = g(n) + h(n) MENOR f(n)

    g = {inicio: 0}
    veio_de = {}

    while fila:
        _, atual = heapq.heappop(fila) # Pega o próx menor f(n)

        if atual == objetivo:
            caminho = []
            # Faz o caminho inverso, vendo de onde o caminho veio
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            return caminho[::-1], g[objetivo]

        for vizinho in grafo[atual]:
            custo = g[atual] + grafo[atual][vizinho]

            if vizinho not in g or custo < g[vizinho]:
                g[vizinho] = custo
                prioridade = custo + heuristicas.get(vizinho, 0)

                heapq.heappush(fila, (prioridade, vizinho))
                veio_de[vizinho] = atual

    return None, float("inf")

def main():
    heuristicas = h()
    grafo = g()

    print(astar(grafo,heuristicas,1,98))

main()