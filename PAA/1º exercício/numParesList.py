import time
import math

def numpares(l):
      inicio = time.time()    # 1
      time.sleep(0.5)           # 1
      pares=[]                     # 1
      for i in l:                      #  n
            if i % 2 == 0:          # n/2
                  pares.append(i)   # n/2
      fim = time.time()             # 1
      return (fim - inicio)*10000.0       # 1


def getValueList():
      valuesList = []
      x = numpares(range(int(math.pow(10,5))))
      y = numpares(range(int(math.pow(10,6))))
      w = numpares(range(int(math.pow(5,6))))
      z = numpares(range(int(math.pow(10,7))))
      k = numpares(range(int(math.pow(5,7))))
      valuesList = [x, y, w, z, k]
      return valuesList
