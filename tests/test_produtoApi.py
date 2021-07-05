import unittest
from lib import produtoApi


class TestProdutoMethods(unittest.TestCase):

    def test_getdadosproduto_sucess(self):
        dto = produtoApi.ProdutoApi().getdadosproduto('15','5880205')
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(dto.data.imagem,'http://imagens.extra.com.br/Control/ArquivoExibir.aspx?IdArquivo=253172122')
        self.assertEqual(dto.data.nome, 'Bola de Natal Santini Christmas 10cm Transparente - 3 Unidades.')
        self.assertEqual(2868, dto.data.categoria)
        self.assertEqual(29.9, dto.data.valor)

    def test_getlistadadosproduto_sucess(self):
        dto = produtoApi.ProdutoApi().getlistadadosproduto('15', ['5880205', '5880206'])
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(dto.data[0].nome, 'Bola de Natal Santini Christmas 8cm Vermelha/Dourada - 6 Unidades.')
        self.assertEqual(dto.data[0].imagem, 'http://imagens.extra.com.br/Control/ArquivoExibir.aspx?IdArquivo=253172225')
        self.assertEqual(2867, dto.data[0].categoria)
        self.assertEqual(22.9, dto.data[0].valor)

    def test_getdadosprodutocampanha_sucess(self):
        dto = produtoApi.ProdutoApi().getdadosprodutocampanha('5940', '5880205', '15', '57.822.975/0001-12')
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual('http://imagens.extra.com.br/Control/ArquivoExibir.aspx?IdArquivo=253172122', dto.data.imagem)
        self.assertEqual('Bola de Natal Santini Christmas 10cm Transparente - 3 Unidades.', dto.data.nome)
        self.assertEqual(2868, dto.data.categoria)
        self.assertEqual(29.9, dto.data.valor)
        self.assertEqual(29.9, dto.data.valorDe)

    def test_getdadosproduto_fail(self):
        dto = produtoApi.ProdutoApi().getdadosproduto('15','595959')
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(dto.error.code,'ProdutoNaoEncontrado')
        self.assertEqual(dto.error.message, 'Produto ou Sku 595959 não encontrado')

    def test_getlistadadosproduto_fail(self):
        dto = produtoApi.ProdutoApi().getlistadadosproduto('15', ['595959'])
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(dto.error.code,'NaoEncontrado')
        self.assertEqual(dto.error.message, 'Nenhum SKU foi encontrado.(ErroValidacao)')

    def test_getdadosprodutocampanha_fail(self):
        dto = produtoApi.ProdutoApi().getdadosprodutocampanha('5940', '59595959', '2', '2')
        print(dto)
        self.assertTrue(dto is not None)
        self.assertEqual(dto.error.code,'400')
        self.assertEqual(dto.error.message, 'A campanha não pertence ao cliente informado.(ErroValidacao)')