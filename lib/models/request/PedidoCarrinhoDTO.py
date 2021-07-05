# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = PedidoCarrinhoDTOfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Produto:
    codigo: Optional[int] = None
    quantidade: Optional[int] = None
    idLojista: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Produto':
        assert isinstance(obj, dict)
        codigo = from_union([from_int, from_none], obj.get("codigo"))
        quantidade = from_union([from_int, from_none], obj.get("quantidade"))
        idLojista = from_union([from_int, from_none], obj.get("idLojista"))
        return Produto(codigo, quantidade, idLojista)

    def to_dict(self) -> dict:
        result: dict = {}
        result["codigo"] = from_union([from_int, from_none], self.codigo)
        result["quantidade"] = from_union([from_int, from_none], self.quantidade)
        result["idLojista"] = from_union([from_int, from_none], self.idLojista)
        return result


@dataclass
class PedidoCarrinhoDTO:
    idCampanha: Optional[int] = None
    cnpj: Optional[str] = None
    cep: Optional[str] = None
    idEntregaTipo: Optional[int] = None
    idEnderecoLojaFisica: Optional[int] = None
    idUnidadeNegocio: Optional[int] = None
    produtos: Optional[List[Produto]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PedidoCarrinhoDTO':
        assert isinstance(obj, dict)
        idCampanha = from_union([from_int, from_none], obj.get("idCampanha"))
        cnpj = from_union([from_str, from_none], obj.get("cnpj"))
        cep = from_union([from_str, from_none], obj.get("cep"))
        idEntregaTipo = from_union([from_int, from_none], obj.get("idEntregaTipo"))
        idEnderecoLojaFisica = from_union([from_int, from_none], obj.get("idEnderecoLojaFisica"))
        idUnidadeNegocio = from_union([from_int, from_none], obj.get("idUnidadeNegocio"))
        produtos = from_union([lambda x: from_list(Produto.from_dict, x), from_none], obj.get("produtos"))
        return PedidoCarrinhoDTO(idCampanha, cnpj, cep, idEntregaTipo, idEnderecoLojaFisica, idUnidadeNegocio, produtos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idCampanha"] = from_union([from_int, from_none], self.idCampanha)
        result["cnpj"] = from_union([from_str, from_none], self.cnpj)
        result["cep"] = from_union([from_str, from_none], self.cep)
        result["idEntregaTipo"] = from_union([from_int, from_none], self.idEntregaTipo)
        result["idEnderecoLojaFisica"] = from_union([from_int, from_none], self.idEnderecoLojaFisica)
        result["idUnidadeNegocio"] = from_union([from_int, from_none], self.idUnidadeNegocio)
        result["produtos"] = from_union([lambda x: from_list(lambda x: to_class(Produto, x), x), from_none], self.produtos)
        return result


def PedidoCarrinhoDTOfromdict(s: Any) -> PedidoCarrinhoDTO:
    return PedidoCarrinhoDTO.from_dict(s)


def PedidoCarrinhoDTOtodict(x: PedidoCarrinhoDTO) -> Any:
    return to_class(PedidoCarrinhoDTO, x)
