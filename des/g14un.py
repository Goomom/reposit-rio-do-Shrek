# Unittest -> É um módulo embutido no Python usado para criar e executar testes automatizados.

# Ex:

# import unittest

# from gA14 import sobrenomeNaOrdem

# class TestSobrenomeNaOrdem(unittest.TestCase):

#     def test_sobrenome_na_ordem(self):
#       NomeCompleto = sobrenomeNaOrdem('Carl', 'Jonhson', 'Smith')
#       self.assertEqual(NomeCompleto, 'Carl, Smith Jonhson')

# unittest.main(argv=[''], exit=False)  # Evita que o unittest chame sys.exit()

# Função passando nos testes

# Se a função passar pelo caso de teste, a saída do seu programa será semelhante à do codigo acima.

# class TestSobrenomeNaOrdem(unittest.TestCase):

#     def test_sobrenome_na_ordem(self):
#       NomeCompleto = sobrenomeNaOrdem('Carl', 'Jonhson', 'Smith')
#       self.assertEqual(NomeCompleto, 'Carl, Smith Jonhson')

#     def test_sobrenome_na_ordem2(self):
#       NomeCompleto = sobrenomeNaOrdem('Carl', 'Tang', 'Li')
#       self.assertEqual(NomeCompleto, 'Carl, Li Tang')

# unittest.main(argv=[''], exit=False)

#  Função não passando nos testes

# Quando há um erro, a saída é bem diferente: informa-se qual é o erro e onde ele está localizado na execução.

# class TestSobrenomeNaOrdem(unittest.TestCase):

#     def test_sobrenome_na_ordem(self):
#       NomeCompleto = sobrenomeNaOrdem('Carl', 'Jonhson', 'Smith')
#       self.assertEqual(NomeCompleto, 'Carl, Jorge Jonhson')

# Outros métodos de unittest     

# assertEqual(a, b) -> Verifica se a e b são iguais.
# assertNotEqual(a, b) -> Verifica se a e b são diferentes.
# assertTrue(x) -> Verifica se x é verdadeiro.
# assertFalse(x) -> Verifica se x é falso.
# assertIn(item, list) -> Verifica se item está presente em list.
# assertNotIn(item, list) -> Verifica se item não está presente em list.

# Testando uma classe

# DPS EU TERMINO, tenho q sair agr