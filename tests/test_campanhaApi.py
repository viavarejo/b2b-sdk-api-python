import unittest
from lib import campanhaApi


class TestCampanhaMethods(unittest.TestCase):

    def test_getcampanhas_sucess(self):
        api = campanhaApi.CampanhaApi()
        dto = api.getcampanhas('2019-08-04', '2100-08-04')
        print(dto)
        self.assertTrue('57.822.975/0001-12', dto.data[0].cnpjContrato)


    def test_getformaspagamento_sucess(self):
        dto = campanhaApi.CampanhaApi().getformaspagamento('5940', '57.822.975/0001-12')
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(1, dto.data[0].idFormaPagamento)
        self.assertEqual('Cartão de Crédito Visa ', dto.data[0].nome)



    def test_getcampanhas_fail(self):
        dto = campanhaApi.CampanhaApi().getcampanhas('2019-08-04', None)
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual('400', dto.error.code)
        self.assertEqual('Request inválido\r\nA dataFim é um parâmetro obrigatório.', dto.error.message)

    #erro fora do padrão
    def test_getformaspagamento_fail(self):
        dto = campanhaApi.CampanhaApi().getformaspagamento('590', '57.822.97-12')
        print(dto)
        self.assertTrue(dto is not None)
        self.assertTrue(not len(dto.data))
        self.assertTrue(dto.error.code is None)



if __name__ == '__main__':
    unittest.main()