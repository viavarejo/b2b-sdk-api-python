import unittest
import random
from typing import Optional

import lib.models.request.PedidoCarrinhoDTO
from lib.api import pedidoApi
from lib.utils.Encryptor import Encryptor
from lib.models.request.ConfirmacaoReqDTO import ConfirmacaoReqDTO
from lib.models.request.CriacaoPedidoReqDTO import CriacaoPedidoReqDTO, Endereco, Destinatario, DadosEntrega
from lib.models.request.PedidoCarrinhoDTO import PedidoCarrinhoDTO
from lib.models.response.CalculoCarrinhoDTO import CalculoCarrinhoDTO
from lib.api import segurancaApi


class DadosPedidoHelper:
    idPedido: Optional[int] = None
    idPedidoParceiro: Optional[int] = None
    idSku: Optional[int] = None
    valorFrete: Optional[float] = None
    precoVenda: Optional[float] = None


class DadosCartaoHelper:
    nome: Optional[str] = None
    numero: Optional[str] = None
    codigoVerificador: Optional[str] = None
    anoValidade: Optional[str] = None
    mesValidade: Optional[str] = None


class TestPedidoMethods(unittest.TestCase):
    id_campanha = 5940
    cnpj = '57.822.975/0001-12'
    cep = '01525000'
    id_sku_criacao_pedido = 8935731
    id_lojista = 15
    id_sku_criacao_pedido_com_cartao = 9342200
    cpf_destinatario = '435.375.660-50'

    pedidoHelper = DadosPedidoHelper()
    pedidocom_cartao_helper = DadosPedidoHelper()
    dadosCartaoHelper = DadosCartaoHelper()

    def test01_calcularcarrinho_paracriarpedido(self):
        produto = lib.models.request.PedidoCarrinhoDTO.Produto()
        produto.codigo = self.id_sku_criacao_pedido
        produto.quantidade = 1
        produto.idLojista = self.id_lojista

        pedidocarrinho = PedidoCarrinhoDTO()
        pedidocarrinho.idCampanha = self.id_campanha
        pedidocarrinho.cnpj = self.cnpj
        pedidocarrinho.cep = self.cep
        pedidocarrinho.produtos = [produto]
        print('Request:')
        print(pedidocarrinho)
        dto = pedidoApi.PedidoApi().postcalcularcarrinho(pedidocarrinho)
        print('Response:')
        print(dto)
        self.assertTrue(dto.data.valorFrete > 0.0)
        self.assertTrue(dto.data.valorTotaldoPedido > 0.0)
        self.pedidoHelper = self.prepara_pedido(dto)
        self.assertTrue(dto.data.produtos[0].valorTotalFrete > 0.0)

    def test02_postcalcularcarrinho_paracriacaoPedidoCartao(self):
        produto = lib.models.request.PedidoCarrinhoDTO.Produto()
        produto.codigo = self.id_sku_criacao_pedido_com_cartao
        produto.quantidade = 1
        produto.idLojista = self.id_lojista

        pedidocarrinho = PedidoCarrinhoDTO()
        pedidocarrinho.idCampanha = self.id_campanha
        pedidocarrinho.cnpj = self.cnpj
        pedidocarrinho.cep = self.cep
        pedidocarrinho.produtos = [produto]
        print('Request:')
        print(pedidocarrinho)
        dto = pedidoApi.PedidoApi().postcalcularcarrinho(pedidocarrinho)
        print('Response:')
        print(dto)
        self.assertTrue(dto.data.valorFrete > 0.0)
        self.assertTrue(dto.data.valorTotaldoPedido > 0.0)
        self.assertTrue(dto.data.produtos[0].valorTotalFrete > 0.0)
        self.pedidocom_cartao_helper = self.prepara_pedido(dto)

    def test03_postcriar_pedido(self):
        request_dto = CriacaoPedidoReqDTO()
        produto = lib.models.request.CriacaoPedidoReqDTO.Produto()
        enderecoEntrega = Endereco()
        destinatario = Destinatario()
        dadosEntrega = DadosEntrega()

        produto.idLojista = self.id_lojista
        produto.codigo = self.pedidoHelper.idSku
        produto.quantidade = 1
        produto.precoVenda = self.pedidoHelper.precoVenda
        produto.premio = 0

        enderecoEntrega.cep = '01525-000'
        enderecoEntrega.estado = 'SP'
        enderecoEntrega.logradouro = 'rua da se'
        enderecoEntrega.cidade = 'São Paulo'
        enderecoEntrega.numero = 63
        enderecoEntrega.referencia = 'teste'
        enderecoEntrega.bairro = 'bairro se'
        enderecoEntrega.complemento = 'teste'
        enderecoEntrega.telefone = '22333333'
        enderecoEntrega.telefone2 = '22333335'
        enderecoEntrega.telefone3 = '22333336'

        destinatario.nome = 'teste'
        destinatario.cpfCnpj = self.cpf_destinatario
        destinatario.email = 'teste@teste.com'

        dadosEntrega.valorFrete = self.pedidoHelper.valorFrete

        request_dto.produtos = [produto]
        request_dto.enderecoEntrega = enderecoEntrega
        request_dto.destinatario = destinatario
        request_dto.dadosEntrega = dadosEntrega
        request_dto.campanha = self.id_campanha
        request_dto.cnpj = self.cnpj
        request_dto.pedidoParceiro = self.gera_id_pedido_parceiro()
        request_dto.valorFrete = self.pedidoHelper.valorFrete
        request_dto.aguardarConfirmacao = True
        request_dto.optantePeloSimples = True
        print('Request:')
        print(request_dto)
        dto = pedidoApi.PedidoApi().postCriarPedido(request_dto)
        print('Response:')
        print(dto)
        valortotal = self.pedidoHelper.valorFrete + self.pedidoHelper.precoVenda
        # self.assertEqual(valortotal, dto.data.valorTotalPedido)
        self.pedidoHelper.idPedido = dto.data.codigoPedido
        self.pedidoHelper.idPedidoParceiro = dto.data.pedidoParceiro

    def test04_postcriar_pedidoCartao(self):
        request_dto = CriacaoPedidoReqDTO()
        produto = lib.models.request.CriacaoPedidoReqDTO.Produto()
        enderecoEntrega = Endereco()
        destinatario = Destinatario()
        dadosEntrega = DadosEntrega()
        pagtosComplementares = lib.models.request.CriacaoPedidoReqDTO.PagtosComplementare()
        dadosCartaoCredito = lib.models.request.CriacaoPedidoReqDTO.DadosCartaoCredito()
        dadosCartaoCreditoValidacao = lib.models.request.CriacaoPedidoReqDTO.DadosCartaoCreditoValidacao()

        produto.idLojista = self.id_lojista
        produto.codigo = self.pedidocom_cartao_helper.idSku
        produto.quantidade = 1
        produto.precoVenda = self.pedidocom_cartao_helper.precoVenda

        enderecoEntrega.cep = '01525-000'
        enderecoEntrega.estado = 'SP'
        enderecoEntrega.logradouro = 'rua da se'
        enderecoEntrega.cidade = 'São Paulo'
        enderecoEntrega.numero = 63
        enderecoEntrega.referencia = 'teste'
        enderecoEntrega.bairro = 'bairro se'
        enderecoEntrega.complemento = 'teste'
        enderecoEntrega.telefone = '22333333'
        enderecoEntrega.telefone2 = '22333335'
        enderecoEntrega.telefone3 = '22333336'

        destinatario.nome = 'teste'
        destinatario.cpfCnpj = self.cpf_destinatario
        destinatario.email = 'teste@teste.com'

        dadosEntrega.valorFrete = self.pedidocom_cartao_helper.valorFrete

        chavedto = segurancaApi.SegurancaApi().getchave()
        chave = chavedto.data.chavePublica
        encryptor = Encryptor()
        encryptor.set_chave(chave)
        dadosCartaoCredito.nome = str(encryptor.encript('Jose da Silva'), 'utf-8')
        dadosCartaoCredito.numero = str(encryptor.encript('5155901222280001'), 'utf-8')
        dadosCartaoCredito.codigoVerificador = str(encryptor.encript('1234'), 'utf-8')
        dadosCartaoCredito.validadeAno = str(encryptor.encript('2045'), 'utf-8')
        dadosCartaoCredito.validadeMes = str(encryptor.encript('12'), 'utf-8')
        dadosCartaoCredito.quantidadeParcelas = 1

        dadosCartaoCreditoValidacao.nome = 'Jose da Silva'
        dadosCartaoCreditoValidacao.numeroMascarado = '515590XXXXXX0001'
        dadosCartaoCreditoValidacao.qtCaracteresCodigoVerificador = '4'
        dadosCartaoCreditoValidacao.validadeAno = '2045'
        dadosCartaoCreditoValidacao.validadeMes = '12'

        pagtosComplementares.idFormaPagamento = 3
        pagtosComplementares.dadosCartaoCredito = dadosCartaoCredito
        pagtosComplementares.dadosCartaoCreditoValidacao = dadosCartaoCreditoValidacao
        pagtosComplementares.valorComplementar = 30.0
        pagtosComplementares.valorComplementarComJuros = 30.0

        request_dto.campanha = self.id_campanha
        request_dto.cnpj = self.cnpj
        request_dto.pedidoParceiro = self.gera_id_pedido_parceiro()
        request_dto.valorFrete = self.pedidocom_cartao_helper.valorFrete
        request_dto.aguardarConfirmacao = True
        request_dto.optantePeloSimples = True
        request_dto.possuiPagtoComplementar = True
        request_dto.produtos = [produto]
        request_dto.enderecoEntrega = enderecoEntrega
        request_dto.destinatario = destinatario
        request_dto.dadosEntrega = dadosEntrega
        request_dto.enderecoCobranca = enderecoEntrega
        request_dto.pagtosComplementares = [pagtosComplementares]
        request_dto.valorTotalPedido = self.pedidocom_cartao_helper.valorFrete + self.pedidocom_cartao_helper.precoVenda
        request_dto.valorTotalComplementar = 30.0
        request_dto.valorTotalComplementarComJuros = 30.0

        print('Request:')
        print(request_dto)
        dto = pedidoApi.PedidoApi().postCriarPedido(request_dto)
        print('Response:')
        print(dto)
        valortotal = self.pedidocom_cartao_helper.valorFrete + self.pedidocom_cartao_helper.precoVenda
        self.assertEqual(valortotal, dto.data.valorTotalPedido)
        self.pedidocom_cartao_helper.idPedido = dto.data.codigoPedido
        self.pedidocom_cartao_helper.idPedidoParceiro = dto.data.pedidoParceiro

    def test05_patch_pedidos_cancelamento(self):
        confirmacao = ConfirmacaoReqDTO()

        confirmacao.idCampanha = self.id_campanha
        confirmacao.idPedidoParceiro = self.pedidoHelper.idPedidoParceiro
        confirmacao.cancelado = True
        confirmacao.confirmado = False
        confirmacao.idPedidoMktplc = '1-01'
        confirmacao.motivoCancelamento = 'teste'
        confirmacao.parceiro = 'BANCO INTER'

        print('Request:')
        print(confirmacao)
        dto = pedidoApi.PedidoApi().patchpedidoscancelamentoconfirmacao(str(self.pedidoHelper.idPedido), confirmacao)
        print('Response:')
        print(dto)
        self.assertTrue(dto.data.pedidoCancelado)

    def test06_patch_pedidos_confirmacao(self):
        confirmacao = ConfirmacaoReqDTO()

        confirmacao.idCampanha = self.id_campanha
        confirmacao.idPedidoParceiro = self.pedidocom_cartao_helper.idPedidoParceiro
        confirmacao.confirmado = True
        print('Request:')
        print(confirmacao)
        dto = pedidoApi.PedidoApi().patchpedidoscancelamentoconfirmacao(str(self.pedidocom_cartao_helper.idPedido),
                                                                        confirmacao)
        print('Response:')
        print(dto)
        self.assertTrue(dto.data.pedidoConfirmado)

    def test07_get_dados_pedido_parceiro(self):
        dto = pedidoApi.PedidoApi().getdadospedidoparceiro(idcompra=str(self.pedidoHelper.idPedido),
                                                           cnpj=self.cnpj,
                                                           idcampanha=str(self.id_campanha),
                                                           idpedidoparceiro=str(self.pedidoHelper.idPedidoParceiro),
                                                           idpedidomktplc=None)
        print('Response:')
        print(dto)
        self.assertEqual(self.pedidoHelper.idPedido, dto.data.pedido.codigoPedido)

    def test08_get_nota_fiscal_pedido_pdf(self):
        dto = pedidoApi.PedidoApi().getNotaFiscalPedido(idcompra='247473612',
                                                        idcompraentrega='91712686',
                                                        formato='PDF')
        self.assertEqual(200, dto.status_code)


    def test09_get_dados_pedido_parceiro_fail(self):
        dto = pedidoApi.PedidoApi().getdadospedidoparceiro(idcompra=str(12),
                                                           cnpj=None,
                                                           idcampanha=None,
                                                           idpedidoparceiro=str(self.pedidoHelper.idPedidoParceiro),
                                                           idpedidomktplc=None)
        self.assertEqual('400', dto.error.code)
        print('Response:')
        print(dto)

    def test10_post_calcularcarrinhoparacriacaopedido_fail(self):
        produto = lib.models.request.PedidoCarrinhoDTO.Produto()
        produto.codigo = None
        produto.quantidade = None
        produto.idLojista = None

        pedidocarrinho = PedidoCarrinhoDTO()
        pedidocarrinho.idCampanha = None
        pedidocarrinho.cnpj = None
        pedidocarrinho.cep = None
        pedidocarrinho.produtos = [produto]
        print('Request:')
        print(pedidocarrinho)
        dto = pedidoApi.PedidoApi().postcalcularcarrinho(pedidocarrinho)
        self.assertEqual('400', dto.error.code)
        print('Response:')
        print(dto)

    def test11_patch_pedidos_fail(self):
        confirmacao = ConfirmacaoReqDTO()

        confirmacao.idCampanha = self.id_campanha
        confirmacao.idPedidoParceiro = None
        confirmacao.cancelado = None
        confirmacao.confirmado = None
        confirmacao.idPedidoMktplc = None
        confirmacao.motivoCancelamento = None
        confirmacao.parceiro = None

        print('Request:')
        print(confirmacao)
        dto = pedidoApi.PedidoApi().patchpedidoscancelamentoconfirmacao(str(self.pedidoHelper.idPedido), confirmacao)
        self.assertEqual('400', dto.error.code)
        print('Response:')
        print(dto)

    def test12_get_nota_fiscal_pedido_fail(self):
        with self.assertRaises(Exception):
            dto = pedidoApi.PedidoApi().getNotaFiscalPedido(idcompra="", idcompraentrega="", formato="")

    def test13_post_criar_pedido_fail(self):
        request_dto = CriacaoPedidoReqDTO()
        produto = lib.models.request.CriacaoPedidoReqDTO.Produto()
        enderecoEntrega = Endereco()
        destinatario = Destinatario()
        dadosEntrega = DadosEntrega()

        produto.idLojista = self.id_lojista
        produto.codigo = None
        produto.quantidade = 1
        produto.precoVenda = self.pedidoHelper.precoVenda
        produto.premio = 0

        enderecoEntrega.cep = '01525-000'
        enderecoEntrega.estado = 'SP'
        enderecoEntrega.logradouro = 'rua da se'
        enderecoEntrega.cidade = 'São Paulo'
        enderecoEntrega.numero = 63
        enderecoEntrega.referencia = 'teste'
        enderecoEntrega.bairro = 'bairro se'
        enderecoEntrega.complemento = 'teste'
        enderecoEntrega.telefone = '22333333'
        enderecoEntrega.telefone2 = '22333335'
        enderecoEntrega.telefone3 = '22333336'

        destinatario.nome = 'teste'
        destinatario.cpfCnpj = self.cpf_destinatario
        destinatario.email = 'teste@teste.com'

        dadosEntrega.valorFrete = self.pedidoHelper.valorFrete

        request_dto.produtos = [produto]
        request_dto.enderecoEntrega = enderecoEntrega
        request_dto.destinatario = destinatario
        request_dto.dadosEntrega = dadosEntrega
        request_dto.campanha = self.id_campanha
        request_dto.cnpj = self.cnpj
        request_dto.pedidoParceiro = self.gera_id_pedido_parceiro()
        request_dto.valorFrete = self.pedidoHelper.valorFrete
        request_dto.aguardarConfirmacao = True
        request_dto.optantePeloSimples = True

        dto = pedidoApi.PedidoApi().postCriarPedido(request_dto)
        self.assertEqual('400', dto.error.code)
        print('Response:')
        print(dto)

    def test_postcriar_pedido(self):
        self.test01_calcularcarrinho_paracriarpedido()
        self.test02_postcalcularcarrinho_paracriacaoPedidoCartao()
        self.test03_postcriar_pedido()
        self.test04_postcriar_pedidoCartao()
        self.test05_patch_pedidos_cancelamento()
        self.test06_patch_pedidos_confirmacao()
        self.test07_get_dados_pedido_parceiro()
        #self.test08_get_nota_fiscal_pedido_pdf()
        self.test09_get_dados_pedido_parceiro_fail()
        self.test10_post_calcularcarrinhoparacriacaopedido_fail()
        self.test11_patch_pedidos_fail()
        self.test12_get_nota_fiscal_pedido_fail()
        self.test13_post_criar_pedido_fail()

    def prepara_pedido(self, calculo: CalculoCarrinhoDTO) -> DadosPedidoHelper:
        helper = DadosPedidoHelper()
        helper.idSku = calculo.data.produtos[0].idSku
        helper.precoVenda = calculo.data.produtos[0].valorUnitario
        helper.valorFrete = calculo.data.produtos[0].valorTotalFrete
        return helper

    def gera_id_pedido_parceiro(self) -> int:
        return random.randint(0, 65536)
