#include <stdio.h>
#include <stdlib.h>

// Número de vértices no grafo
#define V 5

// Função DFS recursiva
void DFS(int graph[V][V], int v, int visited[], int stack[]) {
    visited[v] = 1; // Marque o vértice como visitado

    // Percorra todos os vértices adjacentes a este vértice
    for (int i = 0; i < V; i++) {
        if (graph[v][i] && !visited[i]) {
            DFS(graph, i, visited, stack);
        }
    }

    // Empilhe o vértice atual
    stack[--(*stack)] = v;
}

// Função para realizar a ordenação topológica usando DFS
void topologicalSort(int graph[V][V]) {
    int visited[V];
    for (int i = 0; i < V; i++) {
        visited[i] = 0; // Inicialmente, todos os vértices não foram visitados
    }

    int stack[V];
    int top = V; // Índice do topo da pilha

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            DFS(graph, i, visited, &top);
        }
    }

    // Imprima a ordenação topológica
    printf("Ordenação Topologica:\n");
    while (top < V) {
        printf("%d ", stack[top++]);
    }
    printf("\n");
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

    // Chame a função de ordenação topológica
    topologicalSort(graph);

    return 0;
}
