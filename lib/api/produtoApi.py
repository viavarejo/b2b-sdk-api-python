from lib.utils import rest
from lib.models.ProdutoDTO import ProdutoDTO, ProdutoDTOfromdict
from lib.models.ProdutosDTO import ProdutosDTO, ProdutosDTOfromdict


class ProdutoApi:

    def __init__(self):
        self.client = rest.sapi()

    def getdadosproduto(self, idLogista: str, idSKu: str) -> ProdutoDTO:
        response = self.client.get("/lojistas/"+idLogista+"/produtos/" + idSKu)
        dto = ProdutoDTOfromdict(response)
        return dto

    def getlistadadosproduto(self, idLogista: str, idSKu: []) -> ProdutosDTO:
        querystr = self.queryStringwithArr(idSKu)
        response = self.client.get("/lojistas/"+idLogista+"/produtos/" + querystr)
        dto = ProdutosDTOfromdict(response)
        return dto

    def getdadosprodutocampanha(self, idCampanha:str, idSKu: str, idLojista: str, cnpj: str) -> ProdutoDTO:
        parameters = {
            'idLojista': idLojista,
            'cnpj': cnpj
        }
        response = self.client.get("/campanhas/"+idCampanha+"/produtos/" + idSKu, params=parameters)
        dto = ProdutoDTOfromdict(response)
        return dto


    def queryStringwithArr(self, idSKu: []) -> str:
        queryStr = ''
        for val in idSKu:
            if len(queryStr) == 0:
                queryStr += '?idSKu=' + val
            else:
                queryStr += '&idSKu=' + val
        return queryStr