# Aula 7 - funções 

# Criando funções para declarar uma função utilizamos a palavra reservada: def.
# def nome_da_funcao():
  # Código a ser executado
  # pass

# Função de boas vindas 

# def boas_vindas(): 
#   print('Seja bem vindo!')

# boas_vindas()
# boas_vindas()

# Função com parâmetros

# def boas_vindas_usuario(nome):
#   print('Seja bem-vindo, ' + nome)

  
# boas_vindas_usuario('Paulo')
# boas_vindas_usuario('Mariazinha') 

# Paramêtros são valores passados de fora para dentro de uma função

# Exercícios
# 1 - Crie uma função que exiba uma informação qualquer no console
# 2 - Crie uma função que receba um paramêtro e mostre uma mensagem utilizando este paramêtro

# # 1:
# def boa_tarde():
#   print('Boa tarde ')
        
# boa_tarde()

# # 2:

# def boa_noite(nome):
#   print('Boa noite ' + nome + '!' )

# boa_noite('Carl Jonhson')

# Usando def para somar

# def somar(a , b):
#   print(a + b)

# somar(10 , 25)
# somar(b = 15 , a = 327)

# def velocidade( distancia , tempo):
#   print(distancia / tempo)

# velocidade(20 , 2) 

# Exercícios

# 3 - Crie uma função que pergunte ao usuário dois valores, e depois mostre a soma deles no console

# numero_a = int(input(' DIgite um numero para a soma: \n'))
# numero_b = int(input(' Digite mais um numero: \n'))

# def soma(n1 , n2):
#   print(f'O valor da soma é {n1 + n2}')

# soma(n1 , n2)

# Retornando valores

# *arguments

# def prepara_acai(*itens, tamanho):
#   print('\n Preparando um açaí', tamanho , 'com os seguintes ingredientes:')
#   for ingrediente in itens:
#    print('-', ingrediente)

# prepara_acai('Amendoim' , 'Leite em pó' , 'Marsmallow' , 'Jujuba' , 'Morango' , tamanho = '700ml')
# prepara_acai('Granulado' , 'Chocoball' , 'Morango' , tamanho = '1L')


# Funções que retornam valores
# Para retornar um valor usamos a palavra reservada: return


def diminuir(a , b):
  return a - b


resultado = diminuir(8 ,7)

print(' O resultado da subtração é: ', resultado)

# Funções recursivas
# Função que chama ela mesma até que um problema seja resolvido.

# def dobra_lencol(lencol, gaveta):
#   if lencol < gaveta:
#     return 0
#   else:
#     return 8 + dobra_lencol(lencol / 2, gaveta)
  
# dobra_lencol(200, 25) 

# print(dobra_lencol(200, 25))
