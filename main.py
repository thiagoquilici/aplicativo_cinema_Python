# importar biblioteca
import os

# recebe o nome do usuário
nome = input('Informe seu nome: \n')
idade = int(input ('Informe a sua idade: \n'))

#limpa console
os.system('cls')

while True:
    # Exibe a lista de filmes e suas salas
    print('LISTA DE FILMES\n')
    print('Sala 1 - A volta dos Que Não Foram.\n Classificação indicativa: 16 anos.\n')
    print('Sala 2 - A Roda Quadrada.\n Classificação indicativa: 12 anos.\n')
    print('Sala 3 - Poeira em Alto Mar.\n Classificação indicativa: 14 anos.\n')
    print('Sala 4 - As Tranças do Rei Careca.\n Classificação indicativa: Livre.\n')
    print('Sala 5 - A vingança do Peixe Frito.\n Classificação indicativa: 18 anos.\n')


     # Recebe a sala escolhida
    sala = int(input('Informe a sala desejada:'))

    #limpa console
    os.system('cls')


    match sala:
                case 1:
                     idade_minima = 16
                case 2:
                     idade_minima = 12
                case 3:
                     idade_minima = 14
                case 4:
                     idade_minima = 0
                case 5:
                     idade_minima = 18
                case _:
                    print('Sala inexistente.')
                    

               
 # Verifica as condições
    if idade >= idade_minima:
        print(f'{nome} você está com a entrada autorizada.')
        break

    else:
        print(f'{nome} você não tem idade mínima para assistir a este filme. Por favor, escolha outro.' )
        continue

        

 

    

