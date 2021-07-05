# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = OpcoesParcelamentoDTOfromdict(json.loads(json_string))

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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


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
class Datum:
    idFormaPagamento: Optional[int] = None
    quantidadeParcelas: Optional[int] = None
    taxaJurosAoMes: Optional[float] = None
    valorParcela: Optional[float] = None
    valorTotal: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        idFormaPagamento = from_union([from_int, from_none], obj.get("idFormaPagamento"))
        quantidadeParcelas = from_union([from_int, from_none], obj.get("quantidadeParcelas"))
        taxaJurosAoMes = from_union([from_float, from_none], obj.get("taxaJurosAoMes"))
        valorParcela = from_union([from_float, from_none], obj.get("valorParcela"))
        valorTotal = from_union([from_float, from_none], obj.get("valorTotal"))
        return Datum(idFormaPagamento, quantidadeParcelas, taxaJurosAoMes, valorParcela, valorTotal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idFormaPagamento"] = from_union([from_int, from_none], self.idFormaPagamento)
        result["quantidadeParcelas"] = from_union([from_int, from_none], self.quantidadeParcelas)
        result["taxaJurosAoMes"] = from_union([to_float, from_none], self.taxaJurosAoMes)
        result["valorParcela"] = from_union([to_float, from_none], self.valorParcela)
        result["valorTotal"] = from_union([to_float, from_none], self.valorTotal)
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
class OpcoesParcelamentoDTO:
    data: Optional[List[Datum]] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OpcoesParcelamentoDTO':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return OpcoesParcelamentoDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def OpcoesParcelamentoDTOfromdict(s: Any) -> OpcoesParcelamentoDTO:
    return OpcoesParcelamentoDTO.from_dict(s)


def OpcoesParcelamentoDTOtodict(x: OpcoesParcelamentoDTO) -> Any:
    return to_class(OpcoesParcelamentoDTO, x)
