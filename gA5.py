# Relembrando a aula passada

# Condicionas 

# Condicionas simples

# x = 5
# y = 2

# if x > y:
      # print('O primeiro número é maior')
# else:
     # print('O segundo número é maior')

# % módulo - Retorna o resto da divisão

# print(5 % 2 ) -> 1

# // divisão inteira -  retorna o resultado inteiro da divisão //
# print(5 // 2) -> 2

# ** exponenciação

# print(2 ** 8) -> 256

# Estrutura de repetição ( loops ) 

# For

# for i in range(1 , 11):
#  print(i) -> 1 a 10

# for i in range(1 , 11):
#  print(i , '-Número atual')

# For item in objeto:
#     Faça

# For co  Listas

# lista_de_jogos = ['Minecraft', 'GTA', 'Need for Speed', 'Rocket League' 'Crossfire', 'Battlefield', 'Call of duty', 'ARMA', 'Hell let loose', 'Ready or not', 'Feras to Fathom', 'Gear Club',]

# for jogo in lista_de_jogos:
 #  if jogo[0] == 'C':
   #     print(jogo) -> Apenas jogos que comça com a Inicial escolhida


# Dois codigos que mostram a mesa coisa:

# for jogo in range(len(lista_de_jogos)):
#  print(jogo) -> Mostra quantos jogos tem na lista

# for i in range(len(lista_de_jogos)):
   #      print(lista_de_jogos[i])
# ______________________________________

# lista_de_números = list(range(1 , 100))

# Mostra no console todos os números que forem par entre 1 a 99
# for numero in lista_de_números:
#  if numero % 2 == 0:
#    print(numero)

# frase = 'Nunca sabemos o que terá no amanhã'

# for letra in frase:
#  print(letra) -> Cada letra em uma linha

# while

# x = 0

# while x < 10:
#  print(x)
#  x = x + 1
# x += 1 é a mesma coisa que x = x + 1
# -= / *=

# x = 0

# while x < 500:
#  print('Valor de X: ', x)
#  print('X ainda é menor que 500, vamos somar 1. ')
#  x += 1
#else:+
#  print('FIM! X é igual a 5!')

# Break - continue - Pass 

# Break -> Vai quebrar o loop
# Continue -> Ir para o proximo loop
# Pass -> Não fazer nada

# def fun():
#  pass

# Break 

# for i in range(1, 11):
#  print('Valor Atual:', i)

#  if i == 5:
#    print('Parando o Loop')
#    continue
#  if i == 6:
#    print('Chegou em 6')
#    break
  

# Exercicios
# 1 - Faça uma contagem de 1 a 100 ( Mostre no console ) 

# 2 - Faça um programa que some todos os valores de uma lista

# 3 - Peça ao usuário um número e mostre a tabuada desse número
# 1 a 10

# EXEMPLO

# Escolha do usuário

# saída:

# 1 X 5 = 5
# 2 X 5 = 10
# ...
# 10 X 5= 50

# Exercicio 1

# for i in range(1 , 101):
#   print(i)

# Exercicio 2

# soma = 0
# numeros = list(range(1 , 500))

# for n in numeros:
#   soma += n

# print(soma)