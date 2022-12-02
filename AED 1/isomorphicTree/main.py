class NodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    if not root:
        root = NodeTree(value)
        return root
    fila = []
    fila.append(root)
    while len(fila):
        root = fila[0]
        fila.pop(0)

        if not root.left:
            root.left = NodeTree(value)
            return root
        else:
            fila.append(root.left)
        if not root.right:
            root.right = NodeTree(value)
            return root
        else:
            fila.append(root.right)

def isIsomorphism(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.data != tree2.data:
        return False
    return ((isIsomorphism(tree1.left, tree2.left) and isIsomorphism(tree1.right, tree2.right)) or
            (isIsomorphism(tree1.left, tree2.right) and isIsomorphism(tree1.right, tree2.left)))

if __name__ == '__main__':

    entrada1 = [int(x) if x.replace('\r', '') != "null" else None for x in input().split(",")]
    entrada2 = [int(x) if x.replace('\r', '') != "null" else None for x in input().split(",")]

    arvore1 = None
    for elem in entrada1:
        if arvore1 is None:
            arvore1 = insert(None, elem)
        else:
            insert(arvore1, elem)

    arvore2 = None
    for elem in entrada2:
        if arvore2 is None:
            arvore2 = insert(None, elem)
        else:
            insert(arvore2, elem)

    print("sim" if isIsomorphism(arvore1, arvore2) else "nao")
