from numParesLambda import getValueLambda
from numParesList import getValueList
from plotarGrafico import plotValues


def compararResultados(L1, L2):
      counterL1 = 0
      counterL2 = 0
      mesmoTempo = 0
      results = []
      for x, y in zip(L1, L2):
                  if x > y:
                        results.append(f"L1 --> {x} é maior que L2 --> {y}")
                        counterL1 += 1
                  elif x < y:
                        results.append(f"L1 --> {x} é menor que L2 --> {y}")
                        counterL2 += 1
                  else:
                        results.append(f"L1 --> {x} é igual a L2 --> {y}")
                        mesmoTempo += 1

      for result in results:
            print(result)

      if counterL1 > counterL2:
            print("\nOs tempos de execução da função Lambda são superiores aos da Lista!")
      elif counterL1 < counterL2:
            print("\nOsOs tempos de execução da função Lambda são inferiores aos da Lista!")
      elif counterL1 == counterL2:
             print("\nOsOs tempos de execução de ambos os métodos são iguais!")

      plotValues()

compararResultados(getValueLambda(), getValueList())
