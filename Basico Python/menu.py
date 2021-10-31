import projeto.adivinhacao
import projeto.forca

print("***********************************")
print("****Bem vindo ao menu de jogos!****")
print("***********************************")

opcao=0

while(opcao < 1 or opcao > 2):
    opcao = int(input("Escolha o jogo desejado\n"
                  "(1) Jogo da Adivinhação\n"
                  "(2) Jogo da Forca\n"))

if(opcao == 1):
    print("Jogando Adivinhação")
    projeto.adivinhacao.jogar()

elif(opcao == 2):
    print("Jogando Forca")
    projeto.forca.jogar()
