primeiro_nome = input('digite seu nome \n')
sobrenome_completo = input('digite seu sobrenome completo \n \n')
string1 = sobrenome_completo
print(primeiro_nome)
print(sobrenome_completo)
ultimo_sobrenome = sobrenome_completo.split()[-1]
print("Último sobrenome:", ultimo_sobrenome)

ddd = input('Digite o DDD do seu estado \n')
dddestados = {
    '11': 'São Paulo',
    '21': 'Rio de janeiro',
    '31': 'Minas Gerais',
    '41': 'Paraná',
    '51': 'Rio Grande do Sul',
    '61': 'Distrito Federal',
    '71': 'Bahia',
}
estado = dddestados.get(ddd, 'DDD não encontrado')

print(estado)

cobaias = {
    'coelhos': 10,
    'ratos': 6,
    'sapos': 15
}
total_cobaias = sum(cobaias.values())
print(f'Total de cobaias: {total_cobaias}')
for tipo, quantidade in cobaias.items():
    percentual = (quantidade / total_cobaias) * 100
    print(f'{tipo.capitalize()}: {percentual:.2f}%')

# desafio 2 12/09/25


def saudacao(nome):
    print(f'seja bem vindo {nome}')
nome = input('Digite seu nome: \n')
saudacao(nome)

def dobro(numero):
    return numero * 2
num = int(input('Digite um número: \n'))
print(f'o dobro de {num} é {dobro(num)}')

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
        
num = int(input('Digite um número para calcular o fatorial: \n'))
print(f'O fatorial de {num} é {fatorial(num)}')

def media(n1 , n2 , n3):
    return (n1 + n2 + n3) / 3
num1 = float(input('Digite a primeira nota: \n'))
num2 = float(input('Digite a segunda nota: \n'))
num3 = float(input('Digite a terceira nota: \n'))
print(f' A média das notas é {media(num1, num2, num3)}')

# desafio 22/09/25

# Lê o valor de um arquivo .txt e verifica o intervalo

with open('des/des.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    valor = float(linha.strip())
    if 0 <= valor <= 25:
        print("Intervalo [0,25]")
    elif 25 < valor <= 50:
        print("Intervalo (25,50]")
    elif 50 < valor <= 75:
        print("Intervalo (50,75]")
    elif 75 < valor <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")
                 
V = 1 

N = [0] * 10
N[0] = V

for i in range(1, 10):
    N[i] = N[i-1] * 2

for i in range(10):
    print(f"N[{i}] = {N[i]}")



numero_mes = int(input('Digite um número de 1 a 12: \n')) 
meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

if 1 <= numero_mes <= 12:
    print(meses[numero_mes - 1])
else:
    print("Número de mês inválido")