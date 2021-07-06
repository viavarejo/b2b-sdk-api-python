from lib.utils import rest
from lib.models.SegurancaDTO import SegurancaDTO, SegurancaDTOfromdict


class SegurancaApi:

    def __init__(self):
        self.client = rest.sapi()

    def getchave(self) -> SegurancaDTO:
        response = self.client.get("/seguranca/chaves")
        dto = SegurancaDTOfromdict(response)
        return dto