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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
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


@dataclass
class DadosEntrega:
    previsaoDeEntrega: Optional[str] = None
    valorFrete: Optional[float] = None
    idEntregaTipo: Optional[int] = None
    idEnderecoLojaFisica: Optional[int] = None
    idUnidadeNegocio: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DadosEntrega':
        assert isinstance(obj, dict)
        previsaoDeEntrega = from_union([from_str, from_none], obj.get("previsaoDeEntrega"))
        valorFrete = from_union([from_float, from_none], obj.get("valorFrete"))
        idEntregaTipo = from_union([from_int, from_none], obj.get("idEntregaTipo"))
        idEnderecoLojaFisica = from_union([from_int, from_none], obj.get("idEnderecoLojaFisica"))
        idUnidadeNegocio = from_union([from_int, from_none], obj.get("idUnidadeNegocio"))
        return DadosEntrega(previsaoDeEntrega, valorFrete, idEntregaTipo, idEnderecoLojaFisica, idUnidadeNegocio)

    def to_dict(self) -> dict:
        result: dict = {}
        result["previsaoDeEntrega"] = from_union([from_str, from_none], self.previsaoDeEntrega)
        result["valorFrete"] = from_union([to_float, from_none], self.valorFrete)
        result["idEntregaTipo"] = from_union([from_int, from_none], self.idEntregaTipo)
        result["idEnderecoLojaFisica"] = from_union([from_int, from_none], self.idEnderecoLojaFisica)
        result["idUnidadeNegocio"] = from_union([from_int, from_none], self.idUnidadeNegocio)
        return result


@dataclass
class Pagamento:
    codigoDoErro: Optional[str] = None
    valorComplementar: Optional[float] = None
    quantidadeParcelas: Optional[int] = None
    valorParcela: Optional[float] = None
    idFormaPagamento: Optional[int] = None
    erro: Optional[bool] = None
    mensagemDeErro: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Pagamento':
        assert isinstance(obj, dict)
        codigoDoErro = from_union([from_str, from_none], obj.get("codigoDoErro"))
        valorComplementar = from_union([from_float, from_none], obj.get("valorComplementar"))
        quantidadeParcelas = from_union([from_int, from_none], obj.get("quantidadeParcelas"))
        valorParcela = from_union([from_float, from_none], obj.get("valorParcela"))
        idFormaPagamento = from_union([from_int, from_none], obj.get("idFormaPagamento"))
        erro = from_union([from_bool, from_none], obj.get("erro"))
        mensagemDeErro = from_union([from_str, from_none], obj.get("mensagemDeErro"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Pagamento(codigoDoErro, valorComplementar, quantidadeParcelas, valorParcela, idFormaPagamento, erro, mensagemDeErro, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["codigoDoErro"] = from_union([from_str, from_none], self.codigoDoErro)
        result["valorComplementar"] = from_union([to_float, from_none], self.valorComplementar)
        result["quantidadeParcelas"] = from_union([from_int, from_none], self.quantidadeParcelas)
        result["valorParcela"] = from_union([to_float, from_none], self.valorParcela)
        result["idFormaPagamento"] = from_union([from_int, from_none], self.idFormaPagamento)
        result["erro"] = from_union([from_bool, from_none], self.erro)
        result["mensagemDeErro"] = from_union([from_str, from_none], self.mensagemDeErro)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class DadosPagamentoComplementar:
    pagamentos: Optional[List[Pagamento]] = None
    valorTotalComplementar: Optional[float] = None
    valorTotalComplementarComJuros: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DadosPagamentoComplementar':
        assert isinstance(obj, dict)
        pagamentos = from_union([lambda x: from_list(Pagamento.from_dict, x), from_none], obj.get("pagamentos"))
        valorTotalComplementar = from_union([from_float, from_none], obj.get("valorTotalComplementar"))
        valorTotalComplementarComJuros = from_union([from_float, from_none], obj.get("valorTotalComplementarComJuros"))
        return DadosPagamentoComplementar(pagamentos, valorTotalComplementar, valorTotalComplementarComJuros)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pagamentos"] = from_union([lambda x: from_list(lambda x: to_class(Pagamento, x), x), from_none], self.pagamentos)
        result["valorTotalComplementar"] = from_union([to_float, from_none], self.valorTotalComplementar)
        result["valorTotalComplementarComJuros"] = from_union([to_float, from_none], self.valorTotalComplementarComJuros)
        return result


@dataclass
class Produto:
    idLojista: Optional[int] = None
    codigo: Optional[int] = None
    quantidade: Optional[int] = None
    premio: Optional[float] = None
    precoVenda: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Produto':
        assert isinstance(obj, dict)
        idLojista = from_union([from_int, from_none], obj.get("idLojista"))
        codigo = from_union([from_int, from_none], obj.get("codigo"))
        quantidade = from_union([from_int, from_none], obj.get("quantidade"))
        premio = from_union([from_float, from_none], obj.get("premio"))
        precoVenda = from_union([from_float, from_none], obj.get("precoVenda"))
        return Produto(idLojista, codigo, quantidade, premio, precoVenda)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idLojista"] = from_union([from_int, from_none], self.idLojista)
        result["codigo"] = from_union([from_int, from_none], self.codigo)
        result["quantidade"] = from_union([from_int, from_none], self.quantidade)
        result["premio"] = from_union([to_float, from_none], self.premio)
        result["precoVenda"] = from_union([to_float, from_none], self.precoVenda)
        return result


@dataclass
class Data:
    valorProduto: Optional[float] = None
    valorTotalPedido: Optional[float] = None
    codigoPedido: Optional[int] = None
    pedidoParceiro: Optional[int] = None
    idPedidoMktplc: Optional[str] = None
    produtos: Optional[List[Produto]] = None
    parametrosExtras: Optional[str] = None
    aguardandoConfirmacao: Optional[bool] = None
    dadosEntrega: Optional[DadosEntrega] = None
    dadosPagamentoComplementar: Optional[DadosPagamentoComplementar] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        valorProduto = from_union([from_float, from_none], obj.get("valorProduto"))
        valorTotalPedido = from_union([from_float, from_none], obj.get("valorTotalPedido"))
        codigoPedido = from_union([from_int, from_none], obj.get("codigoPedido"))
        pedidoParceiro = from_union([from_int, from_none], obj.get("pedidoParceiro"))
        idPedidoMktplc = from_union([from_str, from_none], obj.get("idPedidoMktplc"))
        produtos = from_union([lambda x: from_list(Produto.from_dict, x), from_none], obj.get("produtos"))
        parametrosExtras = from_union([from_str, from_none], obj.get("parametrosExtras"))
        aguardandoConfirmacao = from_union([from_bool, from_none], obj.get("aguardandoConfirmacao"))
        dadosEntrega = from_union([DadosEntrega.from_dict, from_none], obj.get("dadosEntrega"))
        dadosPagamentoComplementar = from_union([DadosPagamentoComplementar.from_dict, from_none], obj.get("dadosPagamentoComplementar"))
        return Data(valorProduto, valorTotalPedido, codigoPedido, pedidoParceiro, idPedidoMktplc, produtos, parametrosExtras, aguardandoConfirmacao, dadosEntrega, dadosPagamentoComplementar)

    def to_dict(self) -> dict:
        result: dict = {}
        result["valorProduto"] = from_union([to_float, from_none], self.valorProduto)
        result["valorTotalPedido"] = from_union([to_float, from_none], self.valorTotalPedido)
        result["codigoPedido"] = from_union([from_int, from_none], self.codigoPedido)
        result["pedidoParceiro"] = from_union([from_int, from_none], self.pedidoParceiro)
        result["idPedidoMktplc"] = from_union([from_str, from_none], self.idPedidoMktplc)
        result["produtos"] = from_union([lambda x: from_list(lambda x: to_class(Produto, x), x), from_none], self.produtos)
        result["parametrosExtras"] = from_union([from_str, from_none], self.parametrosExtras)
        result["aguardandoConfirmacao"] = from_union([from_bool, from_none], self.aguardandoConfirmacao)
        result["dadosEntrega"] = from_union([lambda x: to_class(DadosEntrega, x), from_none], self.dadosEntrega)
        result["dadosPagamentoComplementar"] = from_union([lambda x: to_class(DadosPagamentoComplementar, x), from_none], self.dadosPagamentoComplementar)
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
class CriacaoPedidoDTO:
    data: Optional[Data] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CriacaoPedidoDTO':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return CriacaoPedidoDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def CriacaoPedidoDTOfromdict(s: Any) -> CriacaoPedidoDTO:
    return CriacaoPedidoDTO.from_dict(s)


def CriacaoPedidoDTOtodict(x: CriacaoPedidoDTO) -> Any:
    return to_class(CriacaoPedidoDTO, x)
