def par_script(numb):
    result = 0
    for i in range(0, len(numb)):
        result += int(numb[i])
    return result


def imp_script(numb):
    result = -1
    for i in range(0, len(numb)):
        num = int(numb[i])
        if num > result:
            result = num
    return result

numb = int(input(""))
n_dig = len(f"{numb}")
print(n_dig)
if n_dig % 2 == 0:
    print(odd(f"{numb}"))
else:
    print(even(f"{numb}"))