def vira(L, i):
    esquerda = 0
    while esquerda < i:
        L[esquerda], L[i] = L[i], L[esquerda]
        i -= 1
        esquerda += 1


def achar_maior(L, t):
    index = 0
    for i in range(t):
        if L[i] > L[index]:
            index = i
    return index


if __name__ == "__main__":
    L = list(map(int, input().split(",")))
    n = len(L)
    while n > 1:
        maior_index = achar_maior(L, n)
        if maior_index != n:
            vira(L, maior_index)
            vira(L, n - 1)
        n -= 1
    print(",".join(map(str, L)))
