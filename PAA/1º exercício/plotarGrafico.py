import matplotlib.pyplot as plt
from numParesLambda import getValueLambda
from numParesList import getValueList

def plotValues():
    valuesList = getValueList()

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(range(len(valuesList)), valuesList, marker='o')
    plt.title('Tempos de execução da função numPares usando Lista')
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo de execução (ms)')
    plt.xticks(range(len(valuesList)), ['10^5', '10^6', '5x10^6', '10^7', '5x10^7'])

    valuesListLambda = getValueLambda()

    plt.subplot(1, 2, 2)
    plt.plot(range(len(valuesListLambda)), valuesListLambda, marker='o')
    plt.title('Tempos de execução da função numPares usando Lambda')
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo de execução (ms)')
    plt.xticks(range(len(valuesListLambda)), ['10^5', '10^6', '5x10^6', '10^7', '5x10^7'])

    plt.tight_layout()
    plt.show()
