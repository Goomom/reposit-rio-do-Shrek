# Aula 9 - Módulos.

# O que são os módulos?
# - Arquivos usados para segmentar o código e acrescentar mais funcionalidades para a linguagem.

#  Import - Comando usando para importar um módulo.

# 1 - Importando o módulo math .

# import math

# 2 - elevado a 3.
# print(math.pow(2 , 3))

# Arredondando valores.

# Ceil - Arredonda para cima.
# print(math.ceil(2.5))

# Trunc - Arredonda para baixo.
# print(math.trunc(2.5))

# Round - Função nativa do python - Arredonda para o inteiro mais próximo.
# print(round(2.6))
# print(round(2.5))

# 1 - Exercício

# A - Peça ao usuário um número e retorne a raiz quadrada do mesmo número.

# numero = float(input('Digite um número para a Raiz quadrada: \n'))
# import math
# raiz = math.sqrt(numero)
# print(f'A raiz quadrada de {numero} é {raiz}')

# B - Peça ao usuáriro um número decimal e arredonda para o inteiro mais próximo.

# numerodecimal = float(input('Digite um número decimal: \n'))
# print(round(numerodecimal))

# C - Peça ao usuário dois números: Base e expoente. Calcule a potência e retorne o resultado

# numerobase = int(input('Digite um número para ser multiplicado: \n'))
# numeroexpoente = int(input('Digite a quantidade de vezes para ser multiplicado: \n'))

# import math
# print(math.pow(numerobase , numeroexpoente))

# Módulo - OS -> Operation System

# import os

# os.remove - Remove um arquivo - Recebe o caminho do arquivo como paramêtro
# os.remove('./aula9/aula9.txt')


# Verificando se o arquivo existe antes de apaga-lo
# if os.path.exists('./aula9/aula9.txt'):
#      os.remove('./aula9/aula9.txt')
#      print('O arquivo foi removido com sucesso!')
# else:
#      print('Arquivo não existe!')

# rmdir() - Remove uma pasta

# os.rmdir('./aula9/exemplo')

# getcwd() - Retorna o diretório atual
# print('Diretório atual: ', os.getcwd())

# listdir() - Lista todos os arquivos e pastas dentro  de um diretório
# print(os.listdir('./aula9'))

# mkdir() - Cria uma pasta
# rename() - Renomeia uma pasta ou arquivo

# Escrevendo um módulo

# import calculador

# print(calculador.soma(5 , 5))
# print(calculador.subtração(5 , 5))
# print(calculador.divisão(5 , 5))
# print(calculador.multiplicação(5 , 5))

# 2 - Exercícios

# A - Crie um módulo com função para coversão de temperatura; O usuário irá escolher a conversão e o valor ( temperatura ). EX: C para K , 20; A função fará a
# conversão  e retornará o resultado

# Celsius para Kelvin ->  K = C + 273
# Celsius para Fahrenheit -> F = C* 1.8 + 32


# Importando métodos especificos de um módulo

# from calculador import divisão , multiplicação

# print(divisão(2 , 5))
# print(multiplicação(2 , 5))

# import calculador as c

# c.divisão(2)

# Pacotes  - Pasta que irá conter os módulos

# 3 - Exercícios

# Crie um programa que irá gerar uma tabiuada de 0 a 10 a partir de um número escolhido pelo usuário

# EX: 
# imput:5

# Saída:
# 0 X 5 = 0 
# ...
# 10 X 5 = 50

import calculador

numero = int(input('Escolha um número para a tabuada de 0 a 10: \n'))

def multiplicação(a , b):
    return 0 * {numero}
def multiplicação(a , b):
    return 1 * {numero}
def multiplicação(a , b):
    return 2 * {numero}
def multiplicação(a , b):
    return 3 * {numero}
def multiplicação(a , b):
    return 4 * {numero}
def multiplicação(a , b):
    return 5 * {numero}
def multiplicação(a , b):
    return 6 * {numero}
def multiplicação(a , b):
    return 7 * {numero}
def multiplicação(a , b):
    return 8 * {numero}
def multiplicação(a , b):
    return 9 * {numero}
def multiplicação(a , b):
    return 10 * {numero}  
  
print(f'O resultado da tabuada de {numero} é de ')

