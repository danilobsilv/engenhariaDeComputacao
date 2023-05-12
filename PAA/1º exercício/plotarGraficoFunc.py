import matplotlib.pyplot as plt
import numpy as np


def T1(n):
    return 5 + 2*n

def T2(n):
    return 5 + n

x = np.arange(0, 100000001, 10000000) 
y1 = [T1(i) for i in x] 
y2 = [T2(i) for i in x] 

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='T1(n) = 5 + 2n')
plt.plot(x, y2, label='T2(n) = 5 + n')
plt.title('Análise Teórica de Complexidade')
plt.xlabel('Tamanho da entrada (n)')
plt.ylabel('Tempo de execução (T(n))')
plt.legend()
plt.show()
