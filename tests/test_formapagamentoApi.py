import unittest
from lib.api import formapagamentoApi


class TestFormaPagamentoMethods(unittest.TestCase):

    def test_getopcoesparcelamento_sucess(self):
        dto = formapagamentoApi.FormaPagamentoApi().getopcoesparcelamento("1", "5940", "57.822.975/0001-12", "1000")
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(1000.0, dto.data[0].valorParcela)

    #Erro fora do padrão
    def test_getopcoesparcelamento_fail(self):
        dto = formapagamentoApi.FormaPagamentoApi().getopcoesparcelamento("8", "5940", "57.822.975/0001-12", "1000")
        print(dto)
        self.assertTrue(dto is not None)
        self.assertTrue(not len(dto.data))