# Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" para representar dados e comportamentos.

# Class () - São representações ou modelos abstratos de entidades e situações do mundo real.

# Exemplo:

# class Casa():
#     Rua = 'Groove Street',
#     Numero = 157,
#     Cidade = 'Los Santos',
#     Estado = 'LS'

# Atributos - São as características ou propriedades que definem o estado de um objeto.

# Exemplo:

# class Casa():
#     Rua = 'Groove Street',
#     Numero = 157,
#     Cidade = 'Los Santos',
#     CEP = '12345-678'

# Metodos - São as funções ou comportamentos que um objeto pode realizar.

# Exemplo:
# class Casa():
#     Rua = 'Groove Street'
#     Numero = 157
#     Cidade = 'Los Santos'
#     CEP = '12345-678'

#     def endereco_completo(self):
#         return "Endereço Completo: " +self.Rua+", "+str(self.Numero)+", "+self.Cidade+" - CEP: "+self.CEP

# Atividades
# class Arvore():
#     tipo ='Oliveira',
#     tamanho = 'dez metros',
#     frutos = 'azeitonas',
#     familia = 'Oleaceae'

#     def produzir_frutos(self):
#         print('Frutos produzidos')
#         print('A árvore produziu frutos: Azeitonas')

#     def crescer(self):
#         print('Crescendo')
#         print('Crescimento concluído')
#         print('A árvore cresceu 1 metro')

# Minha_arvore = Arvore()

# Minha_arvore.produzir_frutos()

# Minha_arvore.crescer()

# Objetos - São instâncias concretas de uma classe, representando entidades específicas com seus próprios atributos e comportamentos.

# Verificando a classe do objeto

# numero = 1
# print(type(numero))
# Lista = [1, 2, 3]
# print(type(Lista))

# No Terminal, vai te mostrar o seguinte: 

# <class 'int'>
# <class 'list'>

# Exemplo:

# casa1 = Casa()
# print(type(casa1)) #--> <class '__main__.Casa'>

# Acessando os atributo de um objeto
# print(casa1.CEP)

# # Acessando o metodo de um objeto
# print(casa1.endereco_completo())  

# 12345-678
# Endereço Completo: Groove Street, 157, Los Santos - CEP: 12345-678

# Método inicializador - É um método especial que é automaticamente chamado quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto com valores específicos.

# __init__() - É o nome padrão do método inicializador em Python. Ele é definido dentro de uma classe e recebe o parâmetro self, que representa a instância atual do objeto.

# class Casa():
#     def __init__(self, rua, numero, cidade, cep):
#         self.Rua = rua
#         self.Numero = numero
#         self.Cidade = cidade
#         self.CEP = cep

#     def endereco_completo(self):
#         return "Endereço Completo: " +self.Rua+", "+str(self.Numero)+", "+self.Cidade+" - CEP: "+self.CEP

# Instaciando o objeto casa2 com valores diferentes
         
# casa1 = Casa('Grove Street', 157, 'Los Santos', '12345-678') 
# casa2 = Casa('Vinewood', 321, 'Los Angeles', '87654-321')        

# print(casa1.endereco_completo()) --> Endereço Completo Casa 1 : Grove Street, 157, Los Santos - CEP: 12345-678
# print(casa2.endereco_completo()) --> Endereço Completo Casa 2 : Vinewood, 321, Los Angeles - CEP: 87654-321

# Passando argumentos na ordem

# casa3 = Casa('Sunset Boulevard', 456, 'Miami', '54321-987')
# pass

# class Casa():
    
#     imobiliaria = 'Ctrl Imoveis' # Atributo de classe

#     def __init__(self, cidade, bairro, cep):
#         self.cidade = cidade
#         self.bairro = bairro
#         self.cep = cep

#     def endereco_completo(self):
#         return f'Endereço Completo: {self.cidade}, {self.bairro} - CEP: {self.cep}'
    
# casa1 = Casa('Liberty City','Angola', '23167-576')
# casa2 = Casa('Vice City','Ocean Drive', '65432-123')
# casa3 = Casa('Los Santos','Vinewood', '98765-432')  

# print(casa1.imobiliaria) --> Ctrl Imoveis
# print(casa2.imobiliaria) --> Ctrl Imoveis
# print(casa3.imobiliaria) --> Ctrl Imoveis

# Métodos getters e setters -  é importante criar alguns métodos que permitam observar e definir novos valores dos atributos.

# get - definir os métodos que retornam o valor de atributos com o nome “get” seguido do nome do atributo.
# set - é comum nomear os métodos, que permitem atualizar os valores, com o nome “set” seguido do nome do atributo.

# class Casa():
    
#     imobiliaria = 'Ctrl Imoveis' # Atributo de classe

#     def __init__(self, cidade, bairro):
#         self.cidade = cidade
#         self.bairro = bairro
    
#     def getImobiliaria(self):
#         return self.imobiliaria
#     def getCidade(self):
#         return self.cidade
#     def getBairro(self):
#         return self.bairro
    
#     def setImobiliaria(self, i):
#         self.imobiliaria = i
#     def setCidade(self, c):
#         self.cidade = c
#     def setBairro(self, b):
#         self.bairro = b

# class animal():
#     def __init__(self, especie, nome, idade):
#         self.especie = especie
#         self.nome = nome
#         self.idade = idade

#     def getInformacoes(self):
#         Info = (f'Informações do Animal: \n Espécie: {self.especie} \n Nome: {self.nome} \n Idade: {self.idade} anos')
#         return Info
#     def setInformacoes(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# animal1 = animal('Cachorro', 'Big Smoke', 5)
# animal2 = animal('Gato', 'CJ', 3)       
# animal3 = animal('Pássaro', 'Ryder', 2)
# print(animal1.getInformacoes())
# print(animal2.getInformacoes()) 
# print(animal3.getInformacoes())
# animal1.setInformacoes('Little Smoke', 4)
# print(animal1.getInformacoes())