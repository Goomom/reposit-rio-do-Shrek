# Abstração -> A abstração consiste em um ponto super importante dentro de qualquer linguagem Orientada à Objetos. Quando você programa, 
# seus códigos estão lidando com uma representação de um objeto do mundo real.

# Encapsulamento -> É o processo de esconder os detalhes de implementação de um objeto e expor apenas a funcionalidade necessária.

# Ex:

# class A:
#     a = 1 # atributo publico
#     __b = 2 # atributo privado a classe A

# class B(A):    
#     __c = 3 # atributo privado a classe B

#     def __init__(self):
#         print(self.a)
#         print(self.__c)

# a = A()
# print(a.a) # imprime 1

# b = B()
# print(b.__b) # Erro, pois __b é privado a classe A
# print(b.__c) # Errro, __c é um atributo privado, somente chamado pela classe

# Herança -> É o mecanismo que permite que uma classe filha herde atributos e métodos de uma classe pai.

# Ex:

# class Animal():
#     def __init__(self):
#         print('Animal criado')
#     def OqueSou(self):
#         print('Um animal')
#     def come(self):
#         print('Comendo')

# class Cachorro(Animal):
#     def __init__(self):
#         Animal.__init__(self)   
#         print('Cachorro criado')     
#     def OqueSou(self):
#         print('Um cachorro')
#     def late(self):
#         print('AuAu!')    

# # Polimorfismo -> É a habilidade de um método se comportar de maneiras diferentes dependendo do objeto que o está chamando.

# # Exemplo:

# class Animal:
#     def fazer_som(self):
#         raise NotImplementedError("Subclasse deve implementar este método")

# class Gato(Animal):
#     def fazer_som(self):
#         return "Miau!"

# class Cachorro(Animal):
#     def fazer_som(self):
#         return "Au au!"

# class Vaca(Animal):
#     def fazer_som(self):
#         return "Muu!"

# # Uma função que aceita qualquer objeto que tenha o método fazer_som()
# def emitir_som(animal):
#     print(animal.fazer_som())

# # Criação de objetos das subclasses
# gato = Gato()
# cachorro = Cachorro()
# vaca = Vaca()

# # Chamada da função com diferentes objetos
# animais = [gato, cachorro, vaca]
# for animal in animais:
#     emitir_som(animal)
