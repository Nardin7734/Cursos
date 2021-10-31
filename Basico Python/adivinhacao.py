import random

def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("***********************************")

    numero_secreto = random.randrange(1,101)

    dificuldade = 0
    total_tentativas=0
    pontos = 1000

    while (dificuldade < 1 or dificuldade > 3):
        dificuldade_str = input("Escolha um nível de dificuldade:\n(1) Fácil | (2) Normal | (3) Difícil \n")
        dificuldade = int(dificuldade_str)

    if (dificuldade == 1):
        total_tentativas = 20
    elif (dificuldade == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas+1):
        print("Tentativa  {}  de  {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100!")
            continue

        print("Você digitou ", chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou!\nVocê fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto")
            pontos = abs(pontos - chute)

    print("O número secreto era {}".format(numero_secreto))


    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()