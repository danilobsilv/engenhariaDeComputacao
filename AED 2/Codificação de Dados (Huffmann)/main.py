class Node:
    def __init__(self, sheet, left=None, right=None):
        self.sheet = sheet
        self.left = left
        self.right = right

def invert(tab):
    temp = {}
    for x in sorted(tab, key=tab.get, reverse=True):
        temp[x] = tab[x]
    tab = temp
    return tab  

def insercaoCoding(tab: dict):
    
    probs = list(tab.values())
    left, right = [], []
    k_left, k_right = [], []
    tab_left, tab_right = {}, {}

    if len(probs) == 2:
        if probs[0] != probs[1]:
            left.append(probs[0])
            right.append(probs[1])
        else:
            chave = list(tab.keys())
            tab_left[chave[0]] = probs[0]
            tab_right[chave[1]] = probs[1]

    elif len(probs) == 1:
        left.append(probs[0])

    else:
        sub_min = 1


        for ind in range(0, len(probs)):
            sub = abs( sum(probs[0:ind + 1]) - sum(probs[ind + 1:]) )
            if sub_min > sub:
                sub_min = sub
                left = probs[0:ind + 1]
                right = probs[ind + 1:]

    
    for i in tab:
        if tab[i] in left:
            k_left.append(i)
        if tab[i] in right:
            k_right.append(i)

    
    for i in range(len(left)):
        tab_left[k_left[i]] = left[i]

    for i in range(len(right)):
        tab_right[k_right[i]] = right[i]
    
    
    # print(tab_left, tab_right)
    return tab_left, tab_right

def insercao(chart:dict, root:Node):
    esq, dire = insercaoCoding(root.sheet)

    for i in chart:
        if i in esq:
            chart[i] = chart[i] + "0"
        if i in dire:
            chart[i] = chart[i] + "1"
    

    root.left = Node(esq)
    root.right = Node(dire)

    if len(root.left.sheet) != 1:
            insercao(chart,Node(root.left.sheet) )
    if len(root.right.sheet) != 1:
        insercao(chart, Node(root.right.sheet))

def validacao(incripted: str, dic: dict):
    keys = list(dic.values())
    temp = incripted
    incript = ''
    ind = 0

    if len(incripted) == 0:
        print("nao")

    elif len(incripted) == 1:
        if incripted in keys:
            print("sim")
        else:
            print("nao")

    else:
        while len(temp) > 1:
            fatia = temp[0:ind+1]
            if fatia in keys:
                incript += fatia
                temp = temp.removeprefix(fatia)
                ind = 0

            else:
                ind += 1
                continue

        if incript == incripted:
            print("sim")
        else:
            print("nao")


if __name__ == "__main__":
    values = {}
    temp =  {}
    discript  = {}

    n = int(input())

    for _ in range(n):
        symb, probs = input().split(" ")
        values[symb] = float(probs)
    for x in values:
        discript[x] = ""
    root = Node(invert(values))

    insercao(discript, root)
    # print(discript)

    incripted = input()

    validacao(incripted, discript)
