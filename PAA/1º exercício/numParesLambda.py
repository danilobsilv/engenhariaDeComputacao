import time
import math

def numparesL(l):
      pares=[]    # 1
      inicio = time.time()    # 1
      time.sleep(0.5)   # 1
      pares = list(filter(lambda valor: valor % 2 == 0, l)) # 1
      fim = time.time() # 1 
      return (fim - inicio)*10000.0 # 1

def getValueLambda():
      valuesList = []
      x = numparesL(range(int(math.pow(10,5))))
      y = numparesL(range(int(math.pow(10,6))))
      w = numparesL(range(int(math.pow(5,6))))
      z = numparesL(range(int(math.pow(10,7))))
      k = numparesL(range(int(math.pow(5,7))))
      valuesList = [x, y, w, z, k]
      return valuesList
