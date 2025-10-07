# import random 

# senha = ''

# caracteres = 'abcdefghijklmnopqrstuvwxyz1234567890!@$%&*'

# for digito in range(8):
#    caracteres = random.choices
#    senha += caracteres


# print('-' * 20)
# print(senha)
# print('-' * 20)

# import random
# import string

# def gerar_senha(tamanho=12):
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
#     return senha

# tamanho = int(input("Digite o tamanho da senha desejada: "))
# senha = gerar_senha(tamanho)
# print("Senha gerada:", senha)

soma = 0
numeros = []

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
    numeros.append(numero)

if numeros:
    expressao = " + ".join(str(n) for n in numeros)
    print(f"{expressao} = {soma}")
else:
    print("Nenhum número foi informado.")