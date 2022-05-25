import random

def cardValue(carta):
    if carta in ("Dama", "Valete", "Rei"):
        return 10
    return int(carta)


cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "Dama", "Valete", "Rei"]
while True:
    jogador1 = input("Jogador 1: ")
    jogador2 = input("Jogador 2: ")
    carta = {jogador1: [random.choice(cartas)], jogador2: [random.choice(cartas)]}
    
    sumFinish = [0, 0]
    sumFinish[0] += int(cardValue(carta[jogador1][0]))
    sumFinish[1] += int(cardValue(carta[jogador2][0]))
    jogador = 1
    playCard = random.choice(cartas)

    while True:
        if jogador >= 3:
            break
        if jogador == 1:
            print(f"Vez do jogador {jogador}")
            print(f"{jogador1}, suas cartas atuais são {' - '.join(carta[jogador1])}")
            ans = input("Você deseja parar? (sim ou não): ")
            if ans == "sim":
                jogador += 1
            else:
                carta[jogador1].append(playCard)
                sumFinish[0] += cardValue(playCard)
                if sumFinish[0] > 21:
                    print("Você estourou, que azar!")
                    jogador +=1
        if jogador == 2:
            print(f"Vez do jogador {jogador}")
            print(f"{jogador2}, suas cartas atuais são {' - '.join(carta[jogador2])}")
            ans = input("Você deseja parar? (sim ou não): ")
            if ans == "sim":
                jogador += 1
            else:
                carta[jogador2].append(playCard)
                sumFinish[1] += cardValue(playCard)
                if sumFinish[1] > 21:
                    print("Você estourou, que azar!")
                    jogador +=1
        if ans == "não":
            playCard = random.choice(cartas)        

    print(f"sumFinish do jogador 1: {sumFinish[0]}")
    print(f"sumFinish do jogador 2: {sumFinish[1]}")

    result = [0, 0]
    result[0] = sumFinish[0] - 21
    result[1] = sumFinish[1] - 21
    if result[0] > 0 and result[1] > 0:
        print("Os dois jogadores ultrapassaram e perderam!")
    elif result[0] > 0 and result[1] < 0:
        print("O jogador 2 ganhou!")
    elif result[0] < 0 and result[1] > 0:
        print("O jogador 1 ganhou")
    elif result[0] == result[1]:
        print("Os jogadores empataram!")
    else:
        ganhador = jogador1 if result[0]>result[1] else jogador2
        print(f"O jogador {ganhador} é o vencedor!!") 

    nov = input("Deseja jogar novamente? (s/n)")
    if nov == "n":
        break