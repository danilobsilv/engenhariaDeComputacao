#include <stdio.h>
#include <limits.h>

// Número de vértices no grafo
#define V 5

// Função auxiliar para encontrar o vértice com a chave mínima
int minKey(int key[], int mstSet[]) {
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++) {
        if (!mstSet[v] && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }

    return min_index;
}

// Função para imprimir a MST gerada pelo algoritmo de Prim
void printMST(int parent[], int graph[V][V]) {
    printf("Aresta   Peso\n");
    for (int i = 1; i < V; i++) {
        printf("%d - %d    %d\n", parent[i], i, graph[i][parent[i]]);
    }
}

// Função que implementa o algoritmo de Prim
void primMST(int graph[V][V]) {
    int parent[V];  // Array para armazenar a MST
    int key[V];     // Chave utilizada para escolher a aresta de menor peso
    int mstSet[V];  // Conjunto que rastreia os vértices incluídos na MST

    // Inicialize todas as chaves como infinito e mstSet como falso
    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = 0;
    }

    // A chave do primeiro vértice é sempre 0, e ele é a raiz da MST
    key[0] = 0;
    parent[0] = -1;

    // Construa a MST com (V-1) vértices
    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet);

        // Marque o vértice escolhido como processado
        mstSet[u] = 1;

        // Atualize as chaves e o vetor de pais dos vértices adjacentes
        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    // Imprima a MST gerada
    printMST(parent, graph);
}

int main() {
    // Grafo de exemplo representado como matriz de adjacências
    int graph[V][V] = {
        {0, 1, 0, 0, 4},
        {1, 0, 2, 3, 4},
        {0, 2, 0, 1, 0},
        {0, 3, 1, 0, 4},
        {4, 4, 0, 4, 0}
    };

    // Chame a função Prim para encontrar a MST
    primMST(graph);

    return 0;
}
