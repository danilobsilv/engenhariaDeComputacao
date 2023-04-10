from iteration_utilities import unique_everseen, duplicates
from collections import defaultdict


class Verification:

      def isSimple(grafo: dict):
            counter = 0  # contador condicional de não ser um grafo simples

            for key, vertex in grafo.items():
                  index = 0
                  
                  if key in vertex:
                        counter += 1
                  elif vertex.count(vertex[index]) != 1:
                  
                        counter += 1
                  
                  index += 1
            if counter == 0:
                  return 1
            else:
                  return 0


      def isComplete(grafo):
            visitado = set()
            fila = [next(iter(grafo))] 
            
            while fila:
                  vertex = fila.pop(0)
                  if vertex not in visitado:
                        visitado.add(vertex)
                        fila.extend(grafo[vertex])
            
            if visitado != set(grafo.keys()):
                   return 0
    
            for vertex in grafo:
                  if set(grafo[vertex]) != set(grafo.keys()) - {vertex}:
                        return 0

            return 1


      def isConnected(grafo):
            inicial = next(iter(grafo))     # Escolher um vértice pra começar

            visitado = set()    #busca em profundidade tendo como base o vert escolhido
            pilha = [inicial]
            while pilha:
                  vertex = pilha.pop()
                  if vertex not in visitado:
                        visitado.add(vertex)
                        pilha.extend(grafo[vertex])

            if len(visitado) == len(grafo):
                  return 1

            else: return 0


      
      def isRegular(grafo):
            grau = len(grafo[next(iter(grafo))])   # grau do primeiro vértice 
    
            for vertex in grafo:  # ver se todos os verts tem o mesmo grau
                  if len(grafo[vertex]) != grau:
                        return 0
            return 1
 
def binaryToDecimal(binary): 
      print(int(binary, 2))

if __name__ == "__main__":
      grafo = {}
      # results_list = []
      try:
            n = int(input())
            for _ in range(n):
                  entrada = input().split()
                  grafo[entrada[0]] = entrada[1:]

            x = str(Verification.isRegular(grafo)) + str(Verification.isConnected(grafo)) + str(Verification.isComplete(grafo)) + str(Verification.isSimple(grafo))

            binaryToDecimal(x)
      
      except:
            raise Exception
