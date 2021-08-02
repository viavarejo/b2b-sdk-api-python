from lib.utils import rest
from lib.models.request.ConfirmacaoReqDTO import ConfirmacaoReqDTO, ConfirmacaoReqDTOtodict
from lib.models.request.CriacaoPedidoReqDTO import CriacaoPedidoReqDTO, CriacaoPedidoReqDTOtodict
from lib.models.request.PedidoCarrinhoDTO import PedidoCarrinhoDTO, PedidoCarrinhoDTOtodict
from lib.models.response import CriacaoPedidoDTO
from lib.models.response.CalculoCarrinhoDTO import CalculoCarrinhoDTO, CalculoCarrinhoDTOfromdict
from lib.models.response.ConfirmacaoDTO import ConfirmacaoDTOfromdict, ConfirmacaoDTO
from lib.models.response.CriacaoPedidoDTO import CriacaoPedidoDTOfromdict
from lib.models.response.PedidoParceiroDadosDTO import PedidoParceiroDadosDTO, PedidoParceiroDadosDTOfromdict


class PedidoApi:

    def __init__(self):
        self.client = rest.sapi()

    def postcalcularcarrinho(self, pedido: PedidoCarrinhoDTO) -> CalculoCarrinhoDTO:
        data = PedidoCarrinhoDTOtodict(pedido)
        response = self.client.post('/pedidos/carrinho', data=data)
        dto = CalculoCarrinhoDTOfromdict(response)
        return dto

    def getdadospedidoparceiro(self, idcompra: str, cnpj: str, idcampanha: str, idpedidoparceiro: str,
                               idpedidomktplc: str) -> PedidoParceiroDadosDTO:
        parameters = {}

        if cnpj:
            parameters['request.cnpj'] = cnpj
        if idcampanha:
            parameters['request.idCampanha'] = idcampanha
        if idpedidoparceiro:
            parameters['request.idPedidoParceiro'] = idpedidoparceiro
        if idpedidomktplc:
            parameters['request.idPedidoMktplc'] = idpedidomktplc

        response = self.client.get('/pedidos/' + idcompra, params=parameters)
        dto = PedidoParceiroDadosDTOfromdict(response)
        return dto

    def patchpedidoscancelamentoconfirmacao(self, idcompra: str, confirmacao: ConfirmacaoReqDTO) -> ConfirmacaoDTO:
        response = self.client.patch('/pedidos/' + idcompra, data=ConfirmacaoReqDTOtodict(confirmacao))
        dto = ConfirmacaoDTOfromdict(response)
        return dto

    def getNotaFiscalPedido(self, idcompra: str, idcompraentrega: str, formato: str):
        response = self.client.getFile('/pedidos/' + idcompra + '/entregas/' + idcompraentrega + '/nfe/' + formato)

        if response.status_code == 200:
            try:
                filename = idcompra + "_" + idcompraentrega + "." + formato.lower()
                file = open(filename, 'wb')
                file.write(response.content)
                file.close()
            except:
                print("Failed to parse bytes from response to file")

        return response

    def postCriarPedido(self, pedido: CriacaoPedidoReqDTO) -> CriacaoPedidoDTO:
        data = CriacaoPedidoReqDTOtodict(pedido)
        response = self.client.post('/pedidos', data=data)
        dto = CriacaoPedidoDTOfromdict(response)
        return dto
