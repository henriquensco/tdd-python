""" ESTUDO DE TDD COM PYTHON """

import unittest
import calculo

class TestCalculo(unittest.TestCase):

	def test_soma(self):
		self.assertEqual(calculo.soma(10, 5), 15)
		self.assertEqual(calculo.soma(-1, 1), 0)
		self.assertEqual(calculo.soma(-1, -1), -2)

	def test_subtracao(self):
		self.assertEqual(calculo.subtracao(1, 1), 0)
		self.assertEqual(calculo.subtracao(15, 8), 7)
		self.assertEqual(calculo.subtracao(7, 3), 4)

	def test_divisao(self):
		self.assertEqual(calculo.divisao(5, 5), 1)
		self.assertEqual(calculo.divisao(10, 5), 2)
		self.assertEqual(calculo.divisao(10, 2), 5)

	def test_multiplicacao(self):
		self.assertEqual(calculo.multiplicacao(5, 5), 25)
		self.assertEqual(calculo.multiplicacao(6, 3), 18)
		self.assertEqual(calculo.multiplicacao(6, 6), 36)

		with self.assertRaises(ValueError):
			calculo.multiplicacao(10, 5)

if __name__ == '__main__':
	unittest.main()