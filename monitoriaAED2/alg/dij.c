#include <stdio.h>
#include <limits.h>

// Número de vértices no grafo
#define V 5

// Função auxiliar para encontrar o vértice com a distância mínima
int minDistance(int dist[], int sptSet[]) {
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++) {
        if (sptSet[v] == 0 && dist[v] <= min) {
            min = dist[v];
            min_index = v;
        }
    }

    return min_index;
}

// Função para imprimir a solução do algoritmo de Dijkstra
void printSolution(int dist[]) {
    printf("Vértice   Distância da Origem\n");
    for (int i = 0; i < V; i++) {
        printf("%d \t\t %d\n", i, dist[i]);
    }
}

// Função que implementa o algoritmo de Dijkstra
void dijkstra(int graph[V][V], int src) {
    int dist[V];     // Vetor de distâncias mínimas
    int sptSet[V];   // Conjunto de vértices incluídos no caminho mais curto

    // Inicialize todas as distâncias como infinito e sptSet como falso
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = 0;
    }

    // A distância da origem para ela mesma é sempre 0
    dist[src] = 0;

    // Encontre o caminho mais curto para todos os vértices
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet);

        // Marque o vértice escolhido como processado
        sptSet[u] = 1;

        // Atualize distâncias dos vértices adjacentes ao vértice escolhido
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX &&
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // Imprima o vetor de distâncias mínimo
    printSolution(dist);
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

    // Chame a função Dijkstra a partir do vértice 0 (origem)
    dijkstra(graph, 0);

    return 0;
}
