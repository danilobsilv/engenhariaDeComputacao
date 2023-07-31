import matplotlib.pyplot as plt


def convolucao_linear(vetor_XN, vetor_HN):
    result_size = len(vetor_XN) + len(vetor_HN) - 1
    result = []

    for i in range(result_size):
        conv_sum = 0
        for j in range(len(vetor_HN)):
            if i - j >= 0 and i - j < len(vetor_XN):
                conv_sum += vetor_XN[i - j] * vetor_HN[j]
        result.append(conv_sum)

    return result

def read_signal(type):
    vector = [int(input("Sinal: ")) for _ in range(int(input(f"Tamanho do vetor {type}: ")))]
    return vector, int(input(f"Índice inicial do vetor {type}: "))


# sinal de entrada
vetor_XN, XN_index = read_signal("X[N]")

# kernel  
vetor_HN, HN_index = read_signal("H[N]")

# Índice no qual se inicia a resposta Y[N]
YN_index = XN_index + HN_index

# resultado obtido pelo algoritmo implementado acima
resultado = convolucao_linear(vetor_XN, vetor_HN)
print("convolucao_linear --> ", resultado)

# plotagem do gráfico
plt.stem(range(YN_index, YN_index + len(resultado)), resultado)
plt.xlabel('Índice')
plt.ylabel('Amplitude')
plt.title('Convolução Linear')
plt.grid(True)
plt.show()
