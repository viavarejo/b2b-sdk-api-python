# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = PedidoParceiroDadosDTOfromdict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Destinatario:
    nome: Optional[str] = None
    cpfCnpj: Optional[str] = None
    inscricaoEstadual: Optional[str] = None
    email: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Destinatario':
        assert isinstance(obj, dict)
        nome = from_union([from_str, from_none], obj.get("nome"))
        cpfCnpj = from_union([from_str, from_none], obj.get("cpfCnpj"))
        inscricaoEstadual = from_union([from_str, from_none], obj.get("inscricaoEstadual"))
        email = from_union([from_str, from_none], obj.get("email"))
        return Destinatario(nome, cpfCnpj, inscricaoEstadual, email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["cpfCnpj"] = from_union([from_str, from_none], self.cpfCnpj)
        result["inscricaoEstadual"] = from_union([from_str, from_none], self.inscricaoEstadual)
        result["email"] = from_union([from_str, from_none], self.email)
        return result


@dataclass
class Endereco:
    cep: Optional[str] = None
    estado: Optional[str] = None
    logradouro: Optional[str] = None
    cidade: Optional[str] = None
    numero: Optional[int] = None
    referencia: Optional[str] = None
    bairro: Optional[str] = None
    complemento: Optional[str] = None
    telefone: Optional[str] = None
    telefone2: Optional[str] = None
    telefone3: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Endereco':
        assert isinstance(obj, dict)
        cep = from_union([from_str, from_none], obj.get("cep"))
        estado = from_union([from_str, from_none], obj.get("estado"))
        logradouro = from_union([from_str, from_none], obj.get("logradouro"))
        cidade = from_union([from_str, from_none], obj.get("cidade"))
        numero = from_union([from_int, from_none], obj.get("numero"))
        referencia = from_union([from_str, from_none], obj.get("referencia"))
        bairro = from_union([from_str, from_none], obj.get("bairro"))
        complemento = from_union([from_str, from_none], obj.get("complemento"))
        telefone = from_union([from_str, from_none], obj.get("telefone"))
        telefone2 = from_union([from_str, from_none], obj.get("telefone2"))
        telefone3 = from_union([from_str, from_none], obj.get("telefone3"))
        return Endereco(cep, estado, logradouro, cidade, numero, referencia, bairro, complemento, telefone, telefone2, telefone3)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cep"] = from_union([from_str, from_none], self.cep)
        result["estado"] = from_union([from_str, from_none], self.estado)
        result["logradouro"] = from_union([from_str, from_none], self.logradouro)
        result["cidade"] = from_union([from_str, from_none], self.cidade)
        result["numero"] = from_union([from_int, from_none], self.numero)
        result["referencia"] = from_union([from_str, from_none], self.referencia)
        result["bairro"] = from_union([from_str, from_none], self.bairro)
        result["complemento"] = from_union([from_str, from_none], self.complemento)
        result["telefone"] = from_union([from_str, from_none], self.telefone)
        result["telefone2"] = from_union([from_str, from_none], self.telefone2)
        result["telefone3"] = from_union([from_str, from_none], self.telefone3)
        return result


@dataclass
class Motivo:
    categoria: Optional[str] = None
    assunto: Optional[str] = None
    motivo: Optional[str] = None
    observacao: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Motivo':
        assert isinstance(obj, dict)
        categoria = from_union([from_str, from_none], obj.get("categoria"))
        assunto = from_union([from_str, from_none], obj.get("assunto"))
        motivo = from_union([from_str, from_none], obj.get("motivo"))
        observacao = from_union([from_str, from_none], obj.get("observacao"))
        return Motivo(categoria, assunto, motivo, observacao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["categoria"] = from_union([from_str, from_none], self.categoria)
        result["assunto"] = from_union([from_str, from_none], self.assunto)
        result["motivo"] = from_union([from_str, from_none], self.motivo)
        result["observacao"] = from_union([from_str, from_none], self.observacao)
        return result


@dataclass
class ProdutoEntrega:
    codigo: Optional[int] = None
    nome: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[float] = None
    frete: Optional[float] = None
    valorAdicional: Optional[float] = None
    valorTotal: Optional[float] = None
    idLojista: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProdutoEntrega':
        assert isinstance(obj, dict)
        codigo = from_union([from_int, from_none], obj.get("codigo"))
        nome = from_union([from_str, from_none], obj.get("nome"))
        quantidade = from_union([from_int, from_none], obj.get("quantidade"))
        valor = from_union([from_float, from_none], obj.get("valor"))
        frete = from_union([from_float, from_none], obj.get("frete"))
        valorAdicional = from_union([from_float, from_none], obj.get("valorAdicional"))
        valorTotal = from_union([from_float, from_none], obj.get("valorTotal"))
        idLojista = from_union([from_float, from_none], obj.get("idLojista"))
        return ProdutoEntrega(codigo, nome, quantidade, valor, frete, valorAdicional, valorTotal, idLojista)

    def to_dict(self) -> dict:
        result: dict = {}
        result["codigo"] = from_union([from_int, from_none], self.codigo)
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["quantidade"] = from_union([from_int, from_none], self.quantidade)
        result["valor"] = from_union([to_float, from_none], self.valor)
        result["frete"] = from_union([to_float, from_none], self.frete)
        result["valorAdicional"] = from_union([to_float, from_none], self.valorAdicional)
        result["valorTotal"] = from_union([to_float, from_none], self.valorTotal)
        result["idLojista"] = from_union([to_float, from_none], self.idLojista)
        return result


@dataclass
class TrackingEntrega:
    codDescricao: Optional[str] = None
    data: Optional[datetime] = None
    dataEntrega: Optional[datetime] = None
    descricao: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TrackingEntrega':
        assert isinstance(obj, dict)
        codDescricao = from_union([from_str, from_none], obj.get("codDescricao"))
        data = from_union([from_datetime, from_none], obj.get("data"))
        dataEntrega = from_union([from_datetime, from_none], obj.get("dataEntrega"))
        descricao = from_union([from_str, from_none], obj.get("descricao"))
        return TrackingEntrega(codDescricao, data, dataEntrega, descricao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["codDescricao"] = from_union([from_str, from_none], self.codDescricao)
        result["data"] = from_union([lambda x: x.isoformat(), from_none], self.data)
        result["dataEntrega"] = from_union([lambda x: x.isoformat(), from_none], self.dataEntrega)
        result["descricao"] = from_union([from_str, from_none], self.descricao)
        return result


@dataclass
class Entregas:
    codigoEntrega: Optional[float] = None
    previsaoEntrega: Optional[str] = None
    dataEntrega: Optional[str] = None
    dataPrevisao: Optional[str] = None
    dataEmissaoNotaFiscal: Optional[str] = None
    idNotaFiscal: Optional[int] = None
    serieNotaFiscal: Optional[str] = None
    chaveAcesso: Optional[str] = None
    trackingEntrega: Optional[List[TrackingEntrega]] = None
    produtoEntrega: Optional[List[ProdutoEntrega]] = None
    rastreioEntrega: Optional[str] = None
    nomeTransportadora: Optional[str] = None
    linkNotaFiscalPDF: Optional[str] = None
    listNotaFiscalXML: Optional[str] = None
    estorno: Optional[bool] = None
    origem: Optional[str] = None
    motivo: Optional[Motivo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entregas':
        assert isinstance(obj, dict)
        codigoEntrega = from_union([from_float, from_none], obj.get("codigoEntrega"))
        previsaoEntrega = from_union([from_str, from_none], obj.get("previsaoEntrega"))
        dataEntrega = from_union([from_str, from_none], obj.get("dataEntrega"))
        dataPrevisao = from_union([from_str, from_none], obj.get("dataPrevisao"))
        dataEmissaoNotaFiscal = from_union([from_str, from_none], obj.get("dataEmissaoNotaFiscal"))
        idNotaFiscal = from_union([from_int, from_none], obj.get("idNotaFiscal"))
        serieNotaFiscal = from_union([from_str, from_none], obj.get("serieNotaFiscal"))
        chaveAcesso = from_union([from_str, from_none], obj.get("chaveAcesso"))
        trackingEntrega = from_union([lambda x: from_list(TrackingEntrega.from_dict, x), from_none], obj.get("trackingEntrega"))
        produtoEntrega = from_union([lambda x: from_list(ProdutoEntrega.from_dict, x), from_none], obj.get("produtoEntrega"))
        rastreioEntrega = from_union([from_str, from_none], obj.get("rastreioEntrega"))
        nomeTransportadora = from_union([from_str, from_none], obj.get("nomeTransportadora"))
        linkNotaFiscalPDF = from_union([from_str, from_none], obj.get("linkNotaFiscalPDF"))
        listNotaFiscalXML = from_union([from_str, from_none], obj.get("listNotaFiscalXML"))
        estorno = from_union([from_bool, from_none], obj.get("estorno"))
        origem = from_union([from_str, from_none], obj.get("origem"))
        motivo = from_union([Motivo.from_dict, from_none], obj.get("motivo"))
        return Entregas(codigoEntrega, previsaoEntrega, dataEntrega, dataPrevisao, dataEmissaoNotaFiscal, idNotaFiscal, serieNotaFiscal, chaveAcesso, trackingEntrega, produtoEntrega, rastreioEntrega, nomeTransportadora, linkNotaFiscalPDF, listNotaFiscalXML, estorno, origem, motivo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["codigoEntrega"] = from_union([to_float, from_none], self.codigoEntrega)
        result["previsaoEntrega"] = from_union([from_str, from_none], self.previsaoEntrega)
        result["dataEntrega"] = from_union([from_str, from_none], self.dataEntrega)
        result["dataPrevisao"] = from_union([from_str, from_none], self.dataPrevisao)
        result["dataEmissaoNotaFiscal"] = from_union([from_str, from_none], self.dataEmissaoNotaFiscal)
        result["idNotaFiscal"] = from_union([from_int, from_none], self.idNotaFiscal)
        result["serieNotaFiscal"] = from_union([from_str, from_none], self.serieNotaFiscal)
        result["chaveAcesso"] = from_union([from_str, from_none], self.chaveAcesso)
        result["trackingEntrega"] = from_union([lambda x: from_list(lambda x: to_class(TrackingEntrega, x), x), from_none], self.trackingEntrega)
        result["produtoEntrega"] = from_union([lambda x: from_list(lambda x: to_class(ProdutoEntrega, x), x), from_none], self.produtoEntrega)
        result["rastreioEntrega"] = from_union([from_str, from_none], self.rastreioEntrega)
        result["nomeTransportadora"] = from_union([from_str, from_none], self.nomeTransportadora)
        result["linkNotaFiscalPDF"] = from_union([from_str, from_none], self.linkNotaFiscalPDF)
        result["listNotaFiscalXML"] = from_union([from_str, from_none], self.listNotaFiscalXML)
        result["estorno"] = from_union([from_bool, from_none], self.estorno)
        result["origem"] = from_union([from_str, from_none], self.origem)
        result["motivo"] = from_union([lambda x: to_class(Motivo, x), from_none], self.motivo)
        return result


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
    premio: Optional[int] = None
    precoVenda: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Produto':
        assert isinstance(obj, dict)
        idLojista = from_union([from_int, from_none], obj.get("idLojista"))
        codigo = from_union([from_int, from_none], obj.get("codigo"))
        quantidade = from_union([from_int, from_none], obj.get("quantidade"))
        premio = from_union([from_int, from_none], obj.get("premio"))
        precoVenda = from_union([from_float, from_none], obj.get("precoVenda"))
        return Produto(idLojista, codigo, quantidade, premio, precoVenda)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idLojista"] = from_union([from_int, from_none], self.idLojista)
        result["codigo"] = from_union([from_int, from_none], self.codigo)
        result["quantidade"] = from_union([from_int, from_none], self.quantidade)
        result["premio"] = from_union([from_int, from_none], self.premio)
        result["precoVenda"] = from_union([to_float, from_none], self.precoVenda)
        return result


@dataclass
class Pedido:
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
    def from_dict(obj: Any) -> 'Pedido':
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
        return Pedido(valorProduto, valorTotalPedido, codigoPedido, pedidoParceiro, idPedidoMktplc, produtos, parametrosExtras, aguardandoConfirmacao, dadosEntrega, dadosPagamentoComplementar)

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
class Data:
    pedido: Optional[Pedido] = None
    endereco: Optional[Endereco] = None
    destinatario: Optional[Destinatario] = None
    entregas: Optional[List[Entregas]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        pedido = from_union([Pedido.from_dict, from_none], obj.get("pedido"))
        endereco = from_union([Endereco.from_dict, from_none], obj.get("endereco"))
        destinatario = from_union([Destinatario.from_dict, from_none], obj.get("destinatario"))
        entregas = from_union([lambda x: from_list(Entregas.from_dict, x), from_none], obj.get("entregas"))
        return Data(pedido, endereco, destinatario, entregas)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pedido"] = from_union([lambda x: to_class(Pedido, x), from_none], self.pedido)
        result["endereco"] = from_union([lambda x: to_class(Endereco, x), from_none], self.endereco)
        result["destinatario"] = from_union([lambda x: to_class(Destinatario, x), from_none], self.destinatario)
        result["entregas"] = from_union([lambda x: from_list(lambda x: to_class(Entregas, x), x), from_none], self.entregas)
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
class PedidoParceiroDadosDTO:
    data: Optional[Data] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PedidoParceiroDadosDTO':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return PedidoParceiroDadosDTO(data, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def PedidoParceiroDadosDTOfromdict(s: Any) -> PedidoParceiroDadosDTO:
    return PedidoParceiroDadosDTO.from_dict(s)


def PedidoParceiroDadosDTOtodict(x: PedidoParceiroDadosDTO) -> Any:
    return to_class(PedidoParceiroDadosDTO, x)
