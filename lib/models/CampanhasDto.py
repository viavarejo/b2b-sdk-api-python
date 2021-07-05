# and then, to convert JSON from a string, do
#
#     result = CampanhasDTOfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class EntregaTipo:
    idEntregaTipo: Optional[int] = None
    nome: Optional[str] = None
    habilitado: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EntregaTipo':
        assert isinstance(obj, dict)
        idEntregaTipo = from_union([from_int, from_none], obj.get("idEntregaTipo"))
        nome = from_union([from_str, from_none], obj.get("nome"))
        habilitado = from_union([from_bool, from_none], obj.get("habilitado"))
        return EntregaTipo(idEntregaTipo, nome, habilitado)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idEntregaTipo"] = from_union([from_int, from_none], self.idEntregaTipo)
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["habilitado"] = from_union([from_bool, from_none], self.habilitado)
        return result


@dataclass
class Datum:
    idCampanha: Optional[int] = None
    nome: Optional[str] = None
    dataInicio: Optional[datetime] = None
    dataFim: Optional[datetime] = None
    idTipoCampanha: Optional[int] = None
    tipoCampanha: Optional[str] = None
    cnpjContrato: Optional[str] = None
    status: Optional[bool] = None
    entregaTipos: Optional[List[EntregaTipo]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        idCampanha = from_union([from_int, from_none], obj.get("idCampanha"))
        nome = from_union([from_str, from_none], obj.get("nome"))
        dataInicio = from_union([from_datetime, from_none], obj.get("dataInicio"))
        dataFim = from_union([from_datetime, from_none], obj.get("dataFim"))
        idTipoCampanha = from_union([from_int, from_none], obj.get("idTipoCampanha"))
        tipoCampanha = from_union([from_str, from_none], obj.get("tipoCampanha"))
        cnpjContrato = from_union([from_str, from_none], obj.get("cnpjContrato"))
        status = from_union([from_bool, from_none], obj.get("status"))
        entregaTipos = from_union([lambda x: from_list(EntregaTipo.from_dict, x), from_none], obj.get("entregaTipos"))
        return Datum(idCampanha, nome, dataInicio, dataFim, idTipoCampanha, tipoCampanha, cnpjContrato, status, entregaTipos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idCampanha"] = from_union([from_int, from_none], self.idCampanha)
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["dataInicio"] = from_union([lambda x: x.isoformat(), from_none], self.dataInicio)
        result["dataFim"] = from_union([lambda x: x.isoformat(), from_none], self.dataFim)
        result["idTipoCampanha"] = from_union([from_int, from_none], self.idTipoCampanha)
        result["tipoCampanha"] = from_union([from_str, from_none], self.tipoCampanha)
        result["cnpjContrato"] = from_union([from_str, from_none], self.cnpjContrato)
        result["status"] = from_union([from_bool, from_none], self.status)
        result["entregaTipos"] = from_union([lambda x: from_list(lambda x: to_class(EntregaTipo, x), x), from_none], self.entregaTipos)
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
class CampanhasDTO:
    data: Optional[List[Datum]] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CampanhasDTO':
        assert isinstance(obj, dict)
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return CampanhasDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def CampanhasDTOfromdict(s: Any) -> CampanhasDTO:
    return CampanhasDTO.from_dict(s)


def CampanhasDTOtodict(x: CampanhasDTO) -> Any:
    return to_class(CampanhasDTO, x)
