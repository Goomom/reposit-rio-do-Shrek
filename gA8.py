# Aula 08 - Arquivos

# Extensões de arquivos

# .pdf
# .jpeg / .jpg
# .png
# .txt
# .doc

# .py

# abrindo arquivos
# Open() - Recebe o caminho até o arquivo como parâmetro

# arquivo = open('./testt/hal.txt')

# Operações em arquivos
# r( ready only) -> Apenas leitura
# W ( Write only) - > Apenas escrita.
# a ( append ) -> Escreve algo no final do arquivo.
# rt ( read and write ) -> Lê e escreve em um arquivo.

# lendo um arquivo
# read ()
# print(arquivo.read())

# seek(0) -> Volta o ponteiro para o inicio do arquivo
# arquivo.seek(0)

# print(arquivo.read())

# readline() - Lê linhas do arquivo

# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# for i , x in enumerate(arquivo):
#   print(f'Linha {i} - {Linha}')

# arquivo = open('./testt/hal.txt', 'w')
# arquivo.write('Testando a função write')

# Close() -> Fecha o arquivo
# arquivo.close()

# lendo_arquivo = open('./testt/hal.txt')
# print(lendo_arquivo.read())

# Exercícios
# crie uma função que pergunte o nome do usuário e guarde esse nome em um arquivo
# - O nome novo não pode apagar o nome antigo
# - Guarde os nomes em formato de lista
# 
# Ex:
# - Pedro
# - João

# Crie uma segunda função que vai ler todos os nomes no arquivo

# def guarda_nome(name):
#   with open('./name/names.txt', 'a') as arquivo:
#     arquivo.write(name + '\n')   
#   print('O nome foi adicionado com Sucesso!')

# name = input('Qual é o seu nome para ser adicionado a uma list \n')
# guarda_nome(name) 

# def ler_nomes():

#   with open('./name/names.txt') as name:
#     for i , name in enumerate(a)