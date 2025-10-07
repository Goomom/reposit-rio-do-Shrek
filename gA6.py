# Aula 6 ( Tuplas , Sets e Booleanos )
 

# musicas = ('The other side of paradise', 'Enter sandman', 'Wow', 'Natural')

# Tuplas
 # É um tipo de lista que não pode ter seus elemntos alterados.

   # numeros = ( 1 , 2 , 3 , 4 , 5 )

     # dias_da_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')

# Len() - Retorna o tamanho de uma lista
# Count() - Conta quantas vezes um determinado elemento aparece na lista
# Index() - Retorna a posição de um determinado elemento

       # print(dias_da_semana.index('Segunda'))

# Conjuntos (sets)
# Set() - Lista de elementos únicos 

# numeros = set()

# numeros.add(1000)

# print(numeros)

# [] = listas
# {} = Duplas
# {} = sets -  Lista de elementos únicos 

# numero = set()  --> Não está errado

# numero.add(1)
# numero.add(2)
# numero.add(3)
# numero.add(1)
# print(numero)

# or

# numero = set()

# frutas = {'Pera', 'Maça'}
# frutas.add('Uva')


# numero.add(1)
# numero.add(2)
# numero.add(3)
# numero.add(1)
# print(frutas)

# Dicionários - ( Conhecido como "Objetos" em outra linguagens )
# Estrutura que armazena uma chave e um valor.

# pessoa = {
#   'nome': 'CJ',
#   'Idade': 24,
#   'Altura': 1.73,
#   'Idioma': 'Inglês'

# }

# print(pessoa['nome'])
# print(pessoa['Idade'])
# print(pessoa['Altura'])

# pessoa['peso'] = 57

# print(pessoa['peso'])
# print(pessoa['Idioma'])

# carro = {
#   'cor': 'Azul',
#   'motor': 'V8',
#   'Preço': 450.000,
#   'marca': 'BMW'
# }

# Nova_chave = input('O que você gostaria de adiconar ao carro? Potência? Aro? \n--->')

# novo_valor = input('Qual  valor referente a '  + Nova_chave + '? \n--->')

# carro[Nova_chave] = novo_valor
# print(carro)

# Exercícios

# 1 - A partir de uma lista com valores repetidos, crie uma lista com valores únicos



# valores = set()

# valores_misturados = [1 , 2 , 3 , 3 , 2 , 5 , 1 , 4, 5, 54, 11, 48, 7, 8]

# for numero in valores_misturados:
#   valores.add(numero)


# print(valores_misturados) 
# print(valores)

# keys() , values() e items()

# keys() - Apresenta todas as chaves do dicionário
# values() - Apresenta todos os valores armazenados
# items() - Aprsenta ambos

# filme = {
#   'Tema': 'Terror',
#   'Titulo': 'Halloween',
#   'Autor': 'Jonh Carpenter',
# }

# print(filme.keys())
# print(filme.values())
# print(filme.items())

# Exercicio 2 - Crie um Dicionário contendo o DDD e o estado referente. Peça ao usuário digitar um DDD e caso ele exista no dicionário, retorne o estado equivalente, se não, adicione ao dicionário o novo DDD e estado

# DDD_e_estados = {
#   '11': 'São Paulo',
#   '21': 'Rio de Janeiro',
#   '61': 'Brasilia',
#   '68':'Acre',
#   '41':'Paraná',
#   '31': 'Minas gerais'
# }

# ddd = input('Digite o seu DDD: \n--->')

# if ddd in DDD_e_estados:
#   print(f'O estado referente ao DDD {ddd} é {DDD_e_estados[ddd]}')
# else:
#   estado = input('Não encontramos o seu DDD. De qual estado ele seria? \n--->')
#   DDD_e_estados[ddd]
#   print('Novo DDD adicionado. Confira a lista atualizada:', DDD_e_estados)