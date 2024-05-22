
# recebe o nome do usuário
nome = input('Informe seu nome. \n')
idade = int(input ('Informe a sua idade. \n'))

# Exibe a lista de filmes e suas salas
print('LISTA DE FILMES\n')
print('Sala 1 - A volta dos Que Não Foram.\n Classificação indicativa: 16 anos.\n')
print('Sala 2 - A Roda Quadrada.\n Classificação indicativa: 14 anos.\n')
print('Sala 3 - Poeira em Alto Mar.\n Classificação indicativa: 14 anos.\n')
print('Sala 4 - As Tranças do Rei Careca.\n Classificação indicativa: 14 anos.\n')
print('Sala 5 - A vingança do Peixe Frito.\n Classificação indicativa: 16 anos.\n')

# Recebe a sala escolhida
sala = int(input('Informe a sala desejada:'))

match sala:
    case 1:
        print(f'Filme escolhido por {nome}: A Volta dos Que Não Foram.')
    case 2:
        print(f'Filme escolhido por {nome}: A Roda Quadrada.')
    case 3:
        print(f'Filme escolhido por {nome}: Poeira em Alto Mar.')
    case 4:
        print(f'Filme escolhido por {nome}: As Tranças do Rei Careca.')
    case 5:
        print(f'Filme escolhido por {nome}: A vingança do Peixe Frito.')
    case _:
        print('Sala inexistente.')

# Verifica as condições
if idade >= 16:
    print(f'{nome} está com a entrada autorizada.')

else: idade < 14
print(f'{nome} Você não tem idade mínima para assistir a este filme. Por favor, escolha outro.' )
