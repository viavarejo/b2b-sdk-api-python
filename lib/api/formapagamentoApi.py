from lib import rest
from lib.models.OpcoesParcelamentoDTO import OpcoesParcelamentoDTO, OpcoesParcelamentoDTOfromdict


class FormaPagamentoApi:

    def __init__(self):
        self.client = rest.sapi()

    def getopcoesparcelamento(self, idFormaPagamento: str, idCampanha: str, cnpj: str,
                              valorParcelar: str) -> OpcoesParcelamentoDTO:
        parameters = {
            'idCampanha': idCampanha,
            'cnpj': cnpj,
            'valorParcelar': valorParcelar,
        }
        response = self.client.get('/formas-pagamento/' + idFormaPagamento + '/opcoes-parcelamento', params=parameters)
        dto = OpcoesParcelamentoDTOfromdict(response)
        return dto
