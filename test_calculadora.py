# 1) importar a classe calculadora
from calculadora import Calculadora

# 2) importar o pacote de testes unitários
import unittest

#3) criar a classe de testes unitários
class TestCalculadora(unittest.TestCase):
    #4) cria o objeto para
    # herdar a classe calculadora
    # através do metodo chamado setUp
    def setUp(self):
        self.calc = Calculadora()

        # 5) criando o teste
        # do método "soma"
    def test_soma(self):
            self.assertEqual(self.calc.soma(10, 10), 20, "deve somar dois números")
        
        # 6) criando o teste
        # do método "subtracao"
    def test_subtracao(self):
            self.assertEqual(self.calc.subtracao(10, 10), 0, "deve subtrair dois números")

        # 7) criando o teste
        # do método "multiplicacao"
    def test_subtracao(self):
            self.assertEqual(self.calc.multiplicacao(10, 10), 100, "deve multiplicar dois números")

        # 8) criando o teste
        # do método "divisao"
    def test_subtracao(self):
            self.assertEqual(self.calc.divisao(10, 10), 1, "deve dividir dois números")

# executar a classe de testes unitários
if __name__ == "__main__":
    unittest.main()            
