# Erros e Exceções

# Você já encontrou erros em seus programas até este ponto no módulo. Por exemplo:

# print('Ctrl+play)
#       File "<ipython-input-1-06c5efcd28a6>", line 5
#         print('Ctrl+play)

#          SyntaxError: EOL while scanning string literal

# Os erros detectados durante a execução dos programas são chamados de exceções.

# Veja na imagem a seguir, um exemplo de código que pode gerar uma exceção quando ele estiver em execução.
 
# x = input('Digite um número: ')
# y = input('Digite outro número: ')

# print(int(x)/int(y))

 # O que acontece se no programa da Imagem 03 for passado o valor “0” para a variável y? É impossível dividir um número por zero,
# por isso o programa irá lançar uma exceção para o usuário!

# x = input('Digite um número: ')
# y = input('Digite outro número: ')

# print(int(x)/int(y))

# Traceback (most recent call last):
#  File "c:\Users\Guaxi\OneDrive\Desktop\py\des\gA15.py", line 26, in <module>
#     print(int(x)/int(y))
#           ~~~~~~^~~~~~~
# ZeroDivisionError: division by zero

# Para se prevenir desse problema, você terá que utilizar os comandos try except de Python.

#     Try, except e else

# Para lidar com as exceções, você deve colocar o código que pode causar uma delas em um bloco de try: e seu devido tratamento dentro do bloco de except

# try:
#     Você deve tentar algo aqui..
# except Exceção1:
#     Se causar a Exceção1, roda isso.
# except Exceção2:
#     Se causar a Exceção2, roda isso.
# else:
#     Se não causar nenhuma exceção, roda isso.

# Para compreender melhor tudo isso, analise o exemplo do código acima: um código que tenta abrir e depois escrever em um arquivo.

# Se para todas as exceções o tratamento for o mesmo, basta digitar “except: “, sem o nome da exceção.
#  Ao utilizar o comando “except:” dessa forma, você também não precisará decorar o nome de todos os tipos de exceção.

# try:
#     f = open('des.txt', 'w')
#     f.write(' Tenta escreve isto')

# except IOError:
#     # Isso só irá verificar se há uma exceção IOError e,
#     # em seguida, executar esta declaração de impressão.
#     print('Erro: Não foi possível localizar o arquivo')
# else:
#     print('texto escrito com sucesso')    
#     f.close()

#  O código executa os comandos do bloco try e também os comandos no bloco else.

# Agora, veja o que aconteceria se o código não tivesse permissão de escrita (abrindo apenas com 'r'):

# try:
#     f = open('des.txt', 'r')
#     f.write(' Tenta escreve isto')

# except IOError:
#     print('Erro: Não foi possível localizar o arquivo')
# else:
#     print('texto escrito com sucesso')    
#     f.close()

# Ótimo! Observe como é imprimido apenas uma declaração!
# O código ainda continua rodando e é possível continuar o programa fazendo outras ações e cálculos.
#  Bem melhor do que uma tela de erro que trava tudo. 

# UnsurpportedOperation        Trackeback (most recent call last) :
# <ipython-input-3-4e2f5c6e6b3c>, line 72, in <module>()
        
    # f = open('des.txt', 'r')
    # f.write(' Tenta escreve isto')
#       ^^^^^    
    
# Isso é extremamente útil quando houver possíveis erros de entrada em seu código. 
# Você pode estar preparado para o erro e continuar executando o código, em vez de seu código apenas quebrar.    

#   Finally

# O finally é um bloco de código que sempre será executado, independentemente de existir uma exceção no bloco de código try. 
# Sua sintaxe deve ficar como a imagem 09.
# try:
#     Seu código aqui.
#     Se acontece uma exceção aqui
#     O código daqui para baixo pode ser ignorado!
#     Código Ignorado
#     Código Ignorado
#     Código Ignorado
#...
# Finally:
#     Este bloco sempre será executado.

# try:
#     f = open('des.txt', 'w')
#     f.write(' Tenta escreve isto')

# finally:    
#     print('Sempre excuta os comandos do Finally')

# Também é possível usar o finally em conjunto com except. Veja a seguir um novo exemplo que levará em consideração um usuário que coloque a entrada errada

# def Perguntar_Numero():
#     try:
#         val = int(input("Digite um número inteiro: "))
#     except:
#         print("Ops! Isso não é um número inteiro válido. Tente novamente...")    
#     finally:
#         print("Obrigado por usar o programa.")

# Perguntar_Numero()

# Para consertar esse problema, você deve perguntar ao usuário o valor de val até que ele passe um número inteiro válido. Basta criar uma estrutura de repetição!
# def Perguntar_Numero():
#     numero = 1
#     while True:
#         try:
#             val = int(input('Por favor, digite um número inteiro: '))
#         except:
#             print('Ops! Isso não é um número inteiro válido. Tente novamente...')
#             continue
#         else:
#             print('Muito bem!') 
#             break
#         finally:
#             print('Tentativa número:', numero)
#             numero = numero + 1
#     print(val)
# Perguntar_Numero()
