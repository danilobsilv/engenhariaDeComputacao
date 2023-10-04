// Entrada:
// 5 10
// 0 1 10
// 0 3 5
// 1 2 1
// 1 3 2
// 2 4 4
// 3 1 3
// 3 2 9
// 3 4 2
// 4 0 7
// 4 2 6


// Saída:
// 0  esta certo! 
// 8
// 9
// 5
// 7



// Considere um grafo G direcionado e ponderado com pesos não negativos como entrada. Escreva um
// programa em C/C++ que utilize o algoritmo de Dijkstra para determinar os caminhos de custo mínimo
// partindo de um vértice origem do grafo G para todos os demais vértices de G. Como saída, mostre os
// custos de todos esses caminhos mínimos que partem do vértice origem 0 para todos os vértices de G.




#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include<limits.h>

#define V 10  // define o num de vertices


int minDist(int dist[], int set[]){
      int minimal = INT_MAX,  min_index;
      //      || 
      // notação de v para vertices
      for (int v=0; v  < V; v++){
            if (!set[v] && dist[v] <= minimal){
                  minimal = dist[v];
                  min_index = v;
            }
      }
      return min_index;
}


void printSolucao(int dist[], int n){

      printf("\ndistancias minimas a partir do vertice 0: \n");

      for (int i=0; i < V; i++){
            printf("vertice %d: %d\n", i, dist[i]);
      }

}


void dijkstra(int graph[V][V], int src){
      int dist[V];  // distancias minimas
      int set[V];       // controle dos vertices 

      for (int i=0; i < V; i++){
            dist[i] = INT_MAX;
            set[i] = 0;
      }

      dist[src] = 0; // distancia do vertice fonte para ele mesmo vai ser sempre 0;

      for (int contador = 0; contador < V; contador++){
            int u = minDist(dist, set);
            set[u] = 1;

            for (int v = 0; v < V; v++){
                  if (!set[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v] ){
                        dist[v] = dist[u] + graph[u][v];
                  }
            }
      }
      printSolucao(dist, V);
}

int main(){

      int graph[V][V];
      int numVertices, numEdges;

      scanf("%d", &numVertices);
      scanf("%d", &numEdges);

      for (int i=0; i < V; i++){
            for (int j =0; j < V; j++){
                  graph[i][j] = 0;
            }
      }

      for (int i =0; i < numEdges; i++){
            int u, v , peso;

            scanf("%d %d %d", &u, &v, &peso);

            graph[u][v] = peso;
      }

      dijkstra(graph, 0);

      return 0;
}