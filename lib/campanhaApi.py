from lib import rest
from lib.models.CampanhasDto import CampanhasDTO, CampanhasDTOfromdict
from lib.models.FormasPagamentoDTO import FormasPagamentoDTOfromdict, FormasPagamentoDTO


class CampanhaApi:

    def __init__(self):
        self.client = rest.sapi()

    def getcampanhas(self, dtInicio: str, dtFim: str) -> CampanhasDTO:
        parameters = {
            'dataInicio': dtInicio,
            'dataFim': dtFim
        }
        response = self.client.get('/campanhas', params=parameters)
        dto = CampanhasDTOfromdict(response)
        return dto

    def getformaspagamento(self, idCampanha: str, cnpj: str) -> FormasPagamentoDTO:
        parameters = {
            'cnpj': cnpj
        }
        response = self.client.get('/campanhas/' + idCampanha + '/formas-pagamento/opcoes-parcelamento', params=parameters)
        dto = FormasPagamentoDTOfromdict(response)
        return dto
