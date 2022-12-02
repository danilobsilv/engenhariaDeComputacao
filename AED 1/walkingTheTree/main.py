class Node:
    def __init__(self,
                 chave=None):  
        self.chave = chave
        self.esquerda = None
        self.direita = None

def isPrime(n):  
    if n <= 1:
        return
    if n <= 3:
        return False

    if n % 2 == 0 or n % 3 == 0:
        return

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return
        i = i + 6

    return False

def insert(subArvore, node):
    if isPrime(node.chave) == False:  
        return
    else:
        if subArvore is None:
            subArvore = node  

        elif subArvore.chave < node.chave:  
            if subArvore.direita is None:
                subArvore.direita = node
            else:
                insert(subArvore.direita, node)

        else:  
            if subArvore.esquerda is None:
                subArvore.esquerda = node
            else:
                insert(subArvore.esquerda, node)

preordemList = []

def preordemCam(subArvore):
    if subArvore is not None:
        preordemList.append(subArvore.chave)
        preordemCam(subArvore.esquerda)
        preordemCam(subArvore.direita)

inordemList = []

def inordemCam(subArvore):
    if subArvore is not None:
        inordemCam(subArvore.esquerda)
        inordemList.append(subArvore.chave)
        inordemCam(subArvore.direita)

posordemList = []

def posordemCam(subArvore):
    if subArvore is not None:
        posordemCam(subArvore.esquerda)
        posordemCam(subArvore.direita)
        posordemList.append(subArvore.chave)

if __name__ == "__main__":

    entrada1 = input().strip().split(",")
    entrada2 = input().strip().split(",")
    ordem = []

    subArvore = None
    for i in entrada1:
        if subArvore is None:
            subArvore = Node(int(i))
        else:
            no = Node(int(i))
            insert(subArvore, no)

    preordemCam(subArvore)
    inordemCam(subArvore)
    posordemCam(subArvore)

    for i in entrada2:  
        ordem.append(int(i))

    if ordem == preordemList:
        print("pre")
    elif ordem == inordemList:
        print("central")
    elif ordem == posordemList:
        print("pos")
    else:
        print("outro")
