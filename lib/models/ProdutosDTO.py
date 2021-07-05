# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = ProdutosDTOfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class Frete:
    estado: Optional[str] = None
    precoCapital: Optional[str] = None
    precoInterior: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Frete':
        assert isinstance(obj, dict)
        estado = from_union([from_str, from_none], obj.get("estado"))
        precoCapital = from_union([from_str, from_none], obj.get("precoCapital"))
        precoInterior = from_union([from_str, from_none], obj.get("precoInterior"))
        return Frete(estado, precoCapital, precoInterior)

    def to_dict(self) -> dict:
        result: dict = {}
        result["estado"] = from_union([from_str, from_none], self.estado)
        result["precoCapital"] = from_union([from_str, from_none], self.precoCapital)
        result["precoInterior"] = from_union([from_str, from_none], self.precoInterior)
        return result


@dataclass
class DadosEntrega:
    idEntregaTipo: Optional[int] = None
    disponibilidade: Optional[bool] = None
    fretes: Optional[List[Frete]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DadosEntrega':
        assert isinstance(obj, dict)
        idEntregaTipo = from_union([from_int, from_none], obj.get("idEntregaTipo"))
        disponibilidade = from_union([from_bool, from_none], obj.get("disponibilidade"))
        fretes = from_union([lambda x: from_list(Frete.from_dict, x), from_none], obj.get("fretes"))
        return DadosEntrega(idEntregaTipo, disponibilidade, fretes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idEntregaTipo"] = from_union([from_int, from_none], self.idEntregaTipo)
        result["disponibilidade"] = from_union([from_bool, from_none], self.disponibilidade)
        result["fretes"] = from_union([lambda x: from_list(lambda x: to_class(Frete, x), x), from_none], self.fretes)
        return result


@dataclass
class Datum:
    nome: Optional[str] = None
    descricao: Optional[str] = None
    imagem: Optional[str] = None
    categoria: Optional[int] = None
    valor: Optional[float] = None
    valorDe: Optional[float] = None
    disponibilidade: Optional[bool] = None
    foraDeLinha: Optional[bool] = None
    idLojista: Optional[int] = None
    dadosEntrega: Optional[List[DadosEntrega]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        nome = from_union([from_str, from_none], obj.get("nome"))
        descricao = from_union([from_str, from_none], obj.get("descricao"))
        imagem = from_union([from_str, from_none], obj.get("imagem"))
        categoria = from_union([from_int, from_none], obj.get("categoria"))
        valor = from_union([from_float, from_none], obj.get("valor"))
        valorDe = from_union([from_float, from_none], obj.get("valorDe"))
        disponibilidade = from_union([from_bool, from_none], obj.get("disponibilidade"))
        foraDeLinha = from_union([from_bool, from_none], obj.get("foraDeLinha"))
        idLojista = from_union([from_int, from_none], obj.get("idLojista"))
        dadosEntrega = from_union([lambda x: from_list(DadosEntrega.from_dict, x), from_none], obj.get("dadosEntrega"))
        return Datum(nome, descricao, imagem, categoria, valor, valorDe, disponibilidade, foraDeLinha, idLojista, dadosEntrega)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["descricao"] = from_union([from_str, from_none], self.descricao)
        result["imagem"] = from_union([from_str, from_none], self.imagem)
        result["categoria"] = from_union([from_int, from_none], self.categoria)
        result["valor"] = from_union([to_float, from_none], self.valor)
        result["valorDe"] = from_union([to_float, from_none], self.valorDe)
        result["disponibilidade"] = from_union([from_bool, from_none], self.disponibilidade)
        result["foraDeLinha"] = from_union([from_bool, from_none], self.foraDeLinha)
        result["idLojista"] = from_union([from_int, from_none], self.idLojista)
        result["dadosEntrega"] = from_union([lambda x: from_list(lambda x: to_class(DadosEntrega, x), x), from_none], self.dadosEntrega)
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
class ProdutosDTO:
    data: Optional[List[Datum]] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProdutosDTO':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return ProdutosDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def ProdutosDTOfromdict(s: Any) -> ProdutosDTO:
    return ProdutosDTO.from_dict(s)


def ProdutosDTOtodict(x: ProdutosDTO) -> Any:
    return to_class(ProdutosDTO, x)
