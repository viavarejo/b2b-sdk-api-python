# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = CalculoCarrinhoDTOfromdict(json.loads(json_string))

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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Produto:
    idSku: Optional[int] = None
    previsaoEntrega: Optional[str] = None
    valorUnitario: Optional[float] = None
    valorTotal: Optional[float] = None
    valorTotalFrete: Optional[float] = None
    valorTotalImpostos: Optional[float] = None
    erro: Optional[bool] = None
    mensagemDeErro: Optional[str] = None
    codigoDoErro: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Produto':
        assert isinstance(obj, dict)
        idSku = from_union([from_int, from_none], obj.get("idSku"))
        previsaoEntrega = from_union([from_str, from_none], obj.get("previsaoEntrega"))
        valorUnitario = from_union([from_float, from_none], obj.get("valorUnitario"))
        valorTotal = from_union([from_float, from_none], obj.get("valorTotal"))
        valorTotalFrete = from_union([from_float, from_none], obj.get("valorTotalFrete"))
        valorTotalImpostos = from_union([from_float, from_none], obj.get("valorTotalImpostos"))
        erro = from_union([from_bool, from_none], obj.get("erro"))
        mensagemDeErro = from_union([from_str, from_none], obj.get("mensagemDeErro"))
        codigoDoErro = from_union([from_str, from_none], obj.get("codigoDoErro"))
        return Produto(idSku, previsaoEntrega, valorUnitario, valorTotal, valorTotalFrete, valorTotalImpostos, erro, mensagemDeErro, codigoDoErro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idSku"] = from_union([from_int, from_none], self.idSku)
        result["previsaoEntrega"] = from_union([from_str, from_none], self.previsaoEntrega)
        result["valorUnitario"] = from_union([to_float, from_none], self.valorUnitario)
        result["valorTotal"] = from_union([to_float, from_none], self.valorTotal)
        result["valorTotalFrete"] = from_union([to_float, from_none], self.valorTotalFrete)
        result["valorTotalImpostos"] = from_union([to_float, from_none], self.valorTotalImpostos)
        result["erro"] = from_union([from_bool, from_none], self.erro)
        result["mensagemDeErro"] = from_union([from_str, from_none], self.mensagemDeErro)
        result["codigoDoErro"] = from_union([from_str, from_none], self.codigoDoErro)
        return result


@dataclass
class Data:
    valorFrete: Optional[float] = None
    valorImpostos: Optional[float] = None
    valorTotaldosProdutos: Optional[float] = None
    valorTotaldoPedido: Optional[float] = None
    produtos: Optional[List[Produto]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        valorFrete = from_union([from_float, from_none], obj.get("valorFrete"))
        valorImpostos = from_union([from_float, from_none], obj.get("valorImpostos"))
        valorTotaldosProdutos = from_union([from_float, from_none], obj.get("valorTotaldosProdutos"))
        valorTotaldoPedido = from_union([from_float, from_none], obj.get("valorTotaldoPedido"))
        produtos = from_union([lambda x: from_list(Produto.from_dict, x), from_none], obj.get("produtos"))
        return Data(valorFrete, valorImpostos, valorTotaldosProdutos, valorTotaldoPedido, produtos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["valorFrete"] = from_union([to_float, from_none], self.valorFrete)
        result["valorImpostos"] = from_union([to_float, from_none], self.valorImpostos)
        result["valorTotaldosProdutos"] = from_union([to_float, from_none], self.valorTotaldosProdutos)
        result["valorTotaldoPedido"] = from_union([to_float, from_none], self.valorTotaldoPedido)
        result["produtos"] = from_union([lambda x: from_list(lambda x: to_class(Produto, x), x), from_none], self.produtos)
        return result


@dataclass
class Field:
    field: Optional[str] = None
    value: Optional[str] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        field = from_union([from_str, from_none], obj.get("field"))
        value = from_union([from_str, from_none], obj.get("value"))
        message = from_union([from_str, from_none], obj.get("message"))
        return Field(field, value, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["field"] = from_union([from_str, from_none], self.field)
        result["value"] = from_union([from_str, from_none], self.value)
        result["message"] = from_union([from_str, from_none], self.message)
        return result


@dataclass
class Error:
    code: Optional[str] = None
    message: Optional[str] = None
    fields: Optional[List[Field]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        code = from_union([from_str, from_none], obj.get("code"))
        message = from_union([from_str, from_none], obj.get("message"))
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        return Error(code, message, fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_str, from_none], self.code)
        result["message"] = from_union([from_str, from_none], self.message)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        return result


@dataclass
class CalculoCarrinhoDTO:
    data: Optional[Data] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CalculoCarrinhoDTO':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return CalculoCarrinhoDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def CalculoCarrinhoDTOfromdict(s: Any) -> CalculoCarrinhoDTO:
    return CalculoCarrinhoDTO.from_dict(s)


def CalculoCarrinhoDTOtodict(x: CalculoCarrinhoDTO) -> Any:
    return to_class(CalculoCarrinhoDTO, x)
