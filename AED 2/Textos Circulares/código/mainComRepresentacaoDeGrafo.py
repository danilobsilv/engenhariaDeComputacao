import matplotlib.pyplot as plt
import networkx as nx

# Uma modificação do DFS, ou seja um backtracking, para achar o ciclo hamiltoniano do grafo e retornar True se existir
def dfs(L, adj, atual, destino, caminho = ""):
    # Toda vez que um vértice for visitado, ele é adicionado ao caminho
    caminho += f"{atual},"
    # O retorno da função é iniciado com False, pois ele é quem diz se tem algum ciclo hamiltoniano
    ans = False
    # Quantidade de vértices que o caminho atual possui
    vertices_caminho = caminho.split(",")[:-1]

    # Se o vértice atual for o inicial e possuirmos um caminho que passa por todos os vértices, então
    # achamos o ciclo, retornando True
    if atual == destino and len(vertices_caminho) == len(adj) + 1:
        DG = nx.DiGraph()
        for i in range(len(vertices_caminho)-1):
            u = int(vertices_caminho[i])
            v = int(vertices_caminho[i+1])
            DG.add_node(L[u])
            DG.add_edge(L[u], L[v])
        pos = nx.circular_layout(DG)
        nx.draw_networkx_nodes(DG, pos, node_color='lightblue')
        nx.draw_networkx_labels(DG, pos)
        nx.draw_networkx_edges(DG, pos, arrows = True)
        plt.show()
        ans = True
        return ans
    # Loop em que o DFS é aplicado, chamando pela profundidade mais a esquerda
    for i in adj[atual]:
        # Se ans for True, então já encontramos o ciclo e podemos parar de calcular novas possibilidades
        if ans:
            break
        # Se o vertice i não estiver no caminho, então podemos ir até ele
        # Porém, se o vértice já estiver no caminho e ele for a última repetição do vértice inicial para
        # fechar o ciclo, então se permite a sua inclusão
        if f"{i}," not in caminho or (i == destino and len(vertices_caminho) == len(adj)):
            ans = ans or dfs(L, adj, i, destino, caminho)
    # Retorno da funçao
    return ans


# Função temCirculo, que possui como paramêtro a lista L e o tamanho dela N
def temCirculo(L, N):
    # Criação da lista de adjacência do grafo
    DG = nx.DiGraph()
    for str in L:
        DG.add_node(str)
    for i in range(N):
        adj.append(list())
        for j in range(N):
            if i == j:
                continue
            # Considerando duas strings u,v ∈ L , a aresta u→v , existe apenas se o último caractere de u,
            # for igual ao primeiro de v , ou seja, u[−1]==v[0].
            if L[i][-1] == L[j][0]:
                DG.add_edge(L[i], L[j])
                adj[i].append(j)
    pos = nx.circular_layout(DG)
    nx.draw_networkx_nodes(DG, pos, node_color='lightblue')
    nx.draw_networkx_labels(DG, pos)
    nx.draw_networkx_edges(DG, pos, arrows = True)
    plt.show()
    #nx.draw(DG, pos= nx.circular_layout(DG) ,with_labels=True, font_weight='bold')
    #plt.show()

    ans = False
    # Devemos ter como vértice inicial todas as possibilidades, então se encontrarmos alguma
    # já retornamos a resposta
    for i in range(N):
        ans = dfs(L, adj, i, i)
        if ans is True:
            break
    return ans

# Leitura dos dados fornecidos pelo usuário
L = []
adj = []
N = int(input("Informe a quantidade de palavras: "))
for i in range(N):
    L.append(input(f"Informe a palavra {i+1}: "))

# Se a função temCirculo retornar True, então teremos "Sim", se não "Não"
print("Sim" if temCirculo(L, N) else "Não")

