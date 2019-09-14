from unittest import TestCase
from com.leonardo.operacoes import operacoes

class TestOperacoes (TestCase):
   
	def setUp(self):
		self.operacoes = operacoes()
	 
	def test_soma(self):
		self.assertEqual(self.operacoes.soma([1,5]), 6, "should be 6")
	
	def test_div(self):
		self.assertEqual(self.operacoes.divisao([1,5]), 2, "should be 2")