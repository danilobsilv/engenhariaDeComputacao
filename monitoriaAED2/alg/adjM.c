#include <stdio.h>
#include <stdlib.h>

// Estrutura para representar um grafo com matriz de adjacências
struct Graph {
    int V;          // Número de vértices
    int** matrix;   // Matriz de adjacências
};

// Função para criar um novo grafo com V vértices
struct Graph* createGraph(int V) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->V = V;

    // Alocar memória para a matriz de adjacências
    graph->matrix = (int**)malloc(V * sizeof(int*));
    for (int i = 0; i < V; i++) {
        graph->matrix[i] = (int*)malloc(V * sizeof(int));
        for (int j = 0; j < V; j++) {
            // Inicializar todas as arestas como 0 (sem aresta)
            graph->matrix[i][j] = 0;
        }
    }

    return graph;
}

// Função para adicionar uma aresta ao grafo
void addEdge(struct Graph* graph, int src, int dest) {
    // Atribuir 1 à matriz de adjacências para indicar uma aresta entre src e dest
    graph->matrix[src][dest] = 1;
    // Se o grafo for não direcionado, também atribuímos 1 para a aresta de dest para src
    graph->matrix[dest][src] = 1;
}

// Função para imprimir o grafo
void printGraph(struct Graph* graph) {
    printf("Matriz de adjacências do grafo:\n");
    for (int i = 0; i < graph->V; i++) {
        for (int j = 0; j < graph->V; j++) {
            printf("%d ", graph->matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int V = 5; // Número de vértices do grafo
    struct Graph* graph = createGraph(V);

    // Adicionando arestas ao grafo
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);

    // Imprimindo o grafo
    printGraph(graph);

    return 0;
}
