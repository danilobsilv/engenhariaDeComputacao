def sum_script(numb):
    a, b, c = int(numb[0]), int(numb[1]), int(numb[2])

    return a**3 + b**3 + c**3 == int(numb)


for i in range(100, 501):
    if eh(f"{i}"):
        print(i)