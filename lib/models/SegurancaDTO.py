from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Data:
    chavePublica: Optional[str] = None
    dataCadastro: Optional[datetime] = None
    dataExpiracao: Optional[datetime] = None
    dataAtualizacao: Optional[datetime] = None
    ativo: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        chavePublica = from_union([from_str, from_none], obj.get("chavePublica"))
        dataCadastro = from_union([from_datetime, from_none], obj.get("dataCadastro"))
        dataExpiracao = from_union([from_datetime, from_none], obj.get("dataExpiracao"))
        dataAtualizacao = from_union([from_datetime, from_none], obj.get("dataAtualizacao"))
        ativo = from_union([from_bool, from_none], obj.get("ativo"))
        return Data(chavePublica, dataCadastro, dataExpiracao, dataAtualizacao, ativo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chavePublica"] = from_union([from_str, from_none], self.chavePublica)
        result["dataCadastro"] = from_union([lambda x: x.isoformat(), from_none], self.dataCadastro)
        result["dataExpiracao"] = from_union([lambda x: x.isoformat(), from_none], self.dataExpiracao)
        result["dataAtualizacao"] = from_union([lambda x: x.isoformat(), from_none], self.dataAtualizacao)
        result["ativo"] = from_union([from_bool, from_none], self.ativo)
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
class SegurancaDTO:
    data: Optional[Data] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SegurancaDTO':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return SegurancaDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def SegurancaDTOfromdict(s: Any) -> SegurancaDTO:
    return SegurancaDTO.from_dict(s)


def SegurancaDTOtodict(x: SegurancaDTO) -> Any:
    return to_class(SegurancaDTO, x)
