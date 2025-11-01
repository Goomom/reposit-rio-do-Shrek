#nome = input('Olá, primeiramente, como você se chama? ')
#print('Seja bem vindo ' + nome + '!')

#produto = input('O que procura por aqui? ')
#print('Interessante... Irei bsucar para você!')

#estilo = input('Mas antes de eu ir buscar um(a) ' + produto + ' ,digite algo que tenha no(a)' + produto + '!' )
#print('Ótimo!')

#Valor = input('Qual valor desejado? ')
#print('Aqui vai algumas camisas de ' + estilo + ' e o ' + Valor + ' desejado')



# def mostrar_tabuleiro(tab):
#     for linha in tab:
#         print(' | '.join(linha))


# tabuleiro = [['1', '2', '3'], 
#              ['4', '5', '6'], 
#              ['7', '8', '9']]
# jogador_atual = 'X'

# for rodada in range(9):
#     mostrar_tabuleiro(tabuleiro)
#     escolha = input(f'Jogador {jogador_atual}, escolha uma posição (1-9)')
#     pos = int(escolha) -1
#     linha, coluna = pos // 3, pos % 3

#     if tabuleiro[linha][coluna] in ['X', 'O']:
#         print('Posição já ocupada. Tente outra')
#         continue
#     tabuleiro[linha][coluna] = jogador_atual

#     if jogador_atual == 'O':
#      jogador_atual = 'X'
#     else:
#      jogador_atual = 'O'
#     if rodada >= 4:
#        for i in range(3):
#               if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] or \
#                     tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]:
#                       mostrar_tabuleiro(tabuleiro)
#                       print(f'Jogador {jogador_atual} venceu!')
#                       break
#        else:
#            continue
#        break
#     else:
#         mostrar_tabuleiro(tabuleiro)
#         print('Empate!')


# import random
# import string

# def gerar_senha(tamanho):
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     senha = ' '.join(random.choice(caracteres) for _ in range(tamanho))
#     return senha
# tamanho = int(input('Digite o tamanho da senha: '))
# senha = gerar_senha(tamanho)
# print('Senha gerada:', senha)