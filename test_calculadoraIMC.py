from calculadoraIMC import CalculadoraIMC

import unittest

class testCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calcIMC = CalculadoraIMC()

        # testando o método calcular
    def test_calcular(self):
            self.assertEqual(self.calcIMC.calcular(55,180),"Magreza")

if __name__ == "__main__":
    unittest.main()

