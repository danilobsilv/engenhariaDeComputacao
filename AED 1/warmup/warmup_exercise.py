lista = []

num = input()

for simb in num:
    if '(' in simb:
        lista.append(simb)
    if ')' in simb:
        try:
            lista.pop()
        except:
            lista.append('(')

    elif '[' in simb:
        lista.append(simb)
    elif ']' in simb:
        try:
            lista.pop()
        except:
            lista.append(']')

    elif '{' in simb:
        lista.append(simb)
    elif '}' in simb:
        try:
            lista.pop()
        except:
            lista.append('}')


if len(lista) == 0:
    print('1')
elif len(lista) != 0:
    print('0')
