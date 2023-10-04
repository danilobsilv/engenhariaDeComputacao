#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Número de vértices no grafo
#define NUM_VERTICES 5

// Estrutura para representar uma aresta
struct Edge {
    int src, dest, weight;
};

// Estrutura para representar um grafo
struct Graph {
    int V, E;
    struct Edge* edge;
};

// Função para criar um grafo com V vértices e E arestas
struct Graph* createGraph(int V, int E) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->V = V;
    graph->E = E;
    graph->edge = (struct Edge*)malloc(E * sizeof(struct Edge));
    return graph;
}

// Função de comparação para ordenar as arestas em ordem crescente de peso
int compare(const void* a, const void* b) {
    return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}

// Função para encontrar o subconjunto de um elemento "i"
int find(int parent[], int i) {
    if (parent[i] == -1)
        return i;
    return find(parent, parent[i]);
}

// Função para unir dois subconjuntos em um único subconjunto
void Union(int parent[], int x, int y) {
    int xset = find(parent, x);
    int yset = find(parent, y);
    parent[xset] = yset;
}

// Função que implementa o algoritmo de Kruskal
void kruskalMST(struct Graph* graph) {
    int V = graph->V;
    struct Edge result[V];  // Vetor para armazenar as arestas da MST
    int e = 0;              // Índice do vetor de resultado
    int i = 0;              // Índice das arestas classificadas

    // Classifique todas as arestas em ordem crescente de peso
    qsort(graph->edge, graph->E, sizeof(graph->edge[0]), compare);

    // Aloque memória para criar V subconjuntos
    int* parent = (int*)malloc(V * sizeof(int));
    for (int v = 0; v < V; v++)
        parent[v] = -1;

    // Inclua V-1 arestas na MST
    while (e < V - 1 && i < graph->E) {
        struct Edge next_edge = graph->edge[i++];

        int x = find(parent, next_edge.src);
        int y = find(parent, next_edge.dest);

        if (x != y) {
            result[e++] = next_edge;
            Union(parent, x, y);
        }
    }

    // Imprima as arestas da MST
    printf("Aresta   Peso\n");
    for (int j = 0; j < e; j++)
        printf("%d - %d    %d\n", result[j].src, result[j].dest, result[j].weight);
}

int main() {
    // Grafo de exemplo representado como matriz de adjacências
    int graph[NUM_VERTICES][NUM_VERTICES] = {
        {0, 1, 0, 0, 4},
        {1, 0, 2, 3, 4},
        {0, 2, 0, 1, 0},
        {0, 3, 1, 0, 4},
        {4, 4, 0, 4, 0}
    };

    // Crie um grafo e preencha as arestas
    int E = NUM_VERTICES * (NUM_VERTICES - 1) / 2; // No pior caso, grafo completo
    struct Graph* graphData = createGraph(NUM_VERTICES, E);
    int edgeIndex = 0;
    for (int i = 0; i < NUM_VERTICES; i++) {
        for (int j = i + 1; j < NUM_VERTICES; j++) {
            if (graph[i][j] != 0) {
                graphData->edge[edgeIndex].src = i;
                graphData->edge[edgeIndex].dest = j;
                graphData->edge[edgeIndex].weight = graph[i][j];
                edgeIndex++;
            }
        }
    }

    // Chame a função Kruskal para encontrar a MST
    kruskalMST(graphData);

    // Aguarde uma entrada do teclado antes de encerrar o programa
    getchar();

    return 0;
}
