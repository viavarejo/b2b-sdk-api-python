from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ConfirmacaoReqDTO:
    idCampanha: Optional[int] = None
    idPedidoParceiro: Optional[int] = None
    confirmado: Optional[bool] = None
    idPedidoMktplc: Optional[str] = None
    cancelado: Optional[bool] = None
    motivoCancelamento: Optional[str] = None
    parceiro: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConfirmacaoReqDTO':
        assert isinstance(obj, dict)
        idCampanha = from_union([from_int, from_none], obj.get("idCampanha"))
        idPedidoParceiro = from_union([from_int, from_none], obj.get("idPedidoParceiro"))
        confirmado = from_union([from_bool, from_none], obj.get("confirmado"))
        idPedidoMktplc = from_union([from_str, from_none], obj.get("idPedidoMktplc"))
        cancelado = from_union([from_bool, from_none], obj.get("cancelado"))
        motivoCancelamento = from_union([from_str, from_none], obj.get("motivoCancelamento"))
        parceiro = from_union([from_str, from_none], obj.get("parceiro"))
        return ConfirmacaoReqDTO(idCampanha, idPedidoParceiro, confirmado, idPedidoMktplc, cancelado, motivoCancelamento, parceiro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idCampanha"] = from_union([from_int, from_none], self.idCampanha)
        result["idPedidoParceiro"] = from_union([from_int, from_none], self.idPedidoParceiro)
        result["confirmado"] = from_union([from_bool, from_none], self.confirmado)
        result["idPedidoMktplc"] = from_union([from_str, from_none], self.idPedidoMktplc)
        result["cancelado"] = from_union([from_bool, from_none], self.cancelado)
        result["motivoCancelamento"] = from_union([from_str, from_none], self.motivoCancelamento)
        result["parceiro"] = from_union([from_str, from_none], self.parceiro)
        return result


def ConfirmacaoReqDTOfromdict(s: Any) -> ConfirmacaoReqDTO:
    return ConfirmacaoReqDTO.from_dict(s)


def ConfirmacaoReqDTOtodict(x: ConfirmacaoReqDTO) -> Any:
    return to_class(ConfirmacaoReqDTO, x)
