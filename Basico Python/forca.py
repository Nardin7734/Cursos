import random

def jogar():
    imprime_mensagem_abertura()
    palavra = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra)
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0


    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra):
            marca_chute_correto(chute, letras_acertadas, palavra)
        else:
            erros += 1
            print("Você possui {} tentativas".format(len(palavra) - erros))

        enforcou = erros == len(palavra)
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra)


def mensagem_vencedor():
    print("Você ganhou!!")

def mensagem_perdedor(palavra):
    print("A palavra era {}".format(palavra))
    print("Você perdeu!!")

def imprime_mensagem_abertura():
    print("***********************************")
    print("*Bem vindo ao jogo da Forca!*")
    print("***********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Digite uma letra!\n")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra):
    index = 0
    for letra in palavra:
        if (chute.upper() == letra):
            letras_acertadas[index] = letra
        index += 1

if (__name__ == "__main__"):
    jogar()
