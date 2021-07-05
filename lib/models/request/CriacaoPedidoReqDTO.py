from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


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
class DadosCartaoCredito:
    nome: Optional[str] = None
    numero: Optional[str] = None
    codigoVerificador: Optional[str] = None
    validadeAno: Optional[str] = None
    validadeMes: Optional[str] = None
    validadeAnoMes: Optional[str] = None
    quantidadeParcelas: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DadosCartaoCredito':
        assert isinstance(obj, dict)
        nome = from_union([from_str, from_none], obj.get("nome"))
        numero = from_union([from_str, from_none], obj.get("numero"))
        codigoVerificador = from_union([from_str, from_none], obj.get("codigoVerificador"))
        validadeAno = from_union([from_str, from_none], obj.get("validadeAno"))
        validadeMes = from_union([from_str, from_none], obj.get("validadeMes"))
        validadeAnoMes = from_union([from_str, from_none], obj.get("validadeAnoMes"))
        quantidadeParcelas = from_union([from_int, from_none], obj.get("quantidadeParcelas"))
        return DadosCartaoCredito(nome, numero, codigoVerificador, validadeAno, validadeMes, validadeAnoMes, quantidadeParcelas)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["numero"] = from_union([from_str, from_none], self.numero)
        result["codigoVerificador"] = from_union([from_str, from_none], self.codigoVerificador)
        result["validadeAno"] = from_union([from_str, from_none], self.validadeAno)
        result["validadeMes"] = from_union([from_str, from_none], self.validadeMes)
        result["validadeAnoMes"] = from_union([from_str, from_none], self.validadeAnoMes)
        result["quantidadeParcelas"] = from_union([from_int, from_none], self.quantidadeParcelas)
        return result


@dataclass
class DadosCartaoCreditoValidacao:
    nome: Optional[str] = None
    numeroMascarado: Optional[str] = None
    qtCaracteresCodigoVerificador: Optional[str] = None
    validadeAno: Optional[str] = None
    validadeMes: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DadosCartaoCreditoValidacao':
        assert isinstance(obj, dict)
        nome = from_union([from_str, from_none], obj.get("nome"))
        numeroMascarado = from_union([from_str, from_none], obj.get("numeroMascarado"))
        qtCaracteresCodigoVerificador = from_union([from_str, from_none], obj.get("qtCaracteresCodigoVerificador"))
        validadeAno = from_union([from_str, from_none], obj.get("validadeAno"))
        validadeMes = from_union([from_str, from_none], obj.get("validadeMes"))
        return DadosCartaoCreditoValidacao(nome, numeroMascarado, qtCaracteresCodigoVerificador, validadeAno, validadeMes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nome"] = from_union([from_str, from_none], self.nome)
        result["numeroMascarado"] = from_union([from_str, from_none], self.numeroMascarado)
        result["qtCaracteresCodigoVerificador"] = from_union([from_str, from_none], self.qtCaracteresCodigoVerificador)
        result["validadeAno"] = from_union([from_str, from_none], self.validadeAno)
        result["validadeMes"] = from_union([from_str, from_none], self.validadeMes)
        return result


@dataclass
class PagtosComplementare:
    idFormaPagamento: Optional[int] = None
    dadosCartaoCredito: Optional[DadosCartaoCredito] = None
    dadosCartaoCreditoValidacao: Optional[DadosCartaoCreditoValidacao] = None
    valorComplementarComJuros: Optional[float] = None
    valorComplementar: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PagtosComplementare':
        assert isinstance(obj, dict)
        idFormaPagamento = from_union([from_int, from_none], obj.get("idFormaPagamento"))
        dadosCartaoCredito = from_union([DadosCartaoCredito.from_dict, from_none], obj.get("dadosCartaoCredito"))
        dadosCartaoCreditoValidacao = from_union([DadosCartaoCreditoValidacao.from_dict, from_none], obj.get("dadosCartaoCreditoValidacao"))
        valorComplementarComJuros = from_union([from_float, from_none], obj.get("valorComplementarComJuros"))
        valorComplementar = from_union([from_float, from_none], obj.get("valorComplementar"))
        return PagtosComplementare(idFormaPagamento, dadosCartaoCredito, dadosCartaoCreditoValidacao, valorComplementarComJuros, valorComplementar)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idFormaPagamento"] = from_union([from_int, from_none], self.idFormaPagamento)
        result["dadosCartaoCredito"] = from_union([lambda x: to_class(DadosCartaoCredito, x), from_none], self.dadosCartaoCredito)
        result["dadosCartaoCreditoValidacao"] = from_union([lambda x: to_class(DadosCartaoCreditoValidacao, x), from_none], self.dadosCartaoCreditoValidacao)
        result["valorComplementarComJuros"] = from_union([to_float, from_none], self.valorComplementarComJuros)
        result["valorComplementar"] = from_union([to_float, from_none], self.valorComplementar)
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
class CriacaoPedidoReqDTO:
    produtos: Optional[List[Produto]] = None
    enderecoEntrega: Optional[Endereco] = None
    destinatario: Optional[Destinatario] = None
    campanha: Optional[int] = None
    cnpj: Optional[str] = None
    pedidoParceiro: Optional[int] = None
    idPedidoMktplc: Optional[str] = None
    senhaAtendimento: Optional[str] = None
    apolice: Optional[str] = None
    administrador: Optional[int] = None
    parametrosExtras: Optional[str] = None
    valorFrete: Optional[float] = None
    aguardarConfirmacao: Optional[bool] = None
    optantePeloSimples: Optional[bool] = None
    possuiPagtoComplementar: Optional[bool] = None
    pagtosComplementares: Optional[List[PagtosComplementare]] = None
    dadosEntrega: Optional[DadosEntrega] = None
    enderecoCobranca: Optional[Endereco] = None
    valorTotalPedido: Optional[float] = None
    valorTotalComplementar: Optional[float] = None
    valorTotalComplementarComJuros: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CriacaoPedidoReqDTO':
        assert isinstance(obj, dict)
        produtos = from_union([lambda x: from_list(Produto.from_dict, x), from_none], obj.get("produtos"))
        enderecoEntrega = from_union([Endereco.from_dict, from_none], obj.get("enderecoEntrega"))
        destinatario = from_union([Destinatario.from_dict, from_none], obj.get("destinatario"))
        campanha = from_union([from_int, from_none], obj.get("campanha"))
        cnpj = from_union([from_str, from_none], obj.get("cnpj"))
        pedidoParceiro = from_union([from_int, from_none], obj.get("pedidoParceiro"))
        idPedidoMktplc = from_union([from_str, from_none], obj.get("idPedidoMktplc"))
        senhaAtendimento = from_union([from_str, from_none], obj.get("senhaAtendimento"))
        apolice = from_union([from_str, from_none], obj.get("apolice"))
        administrador = from_union([from_int, from_none], obj.get("administrador"))
        parametrosExtras = from_union([from_str, from_none], obj.get("parametrosExtras"))
        valorFrete = from_union([from_float, from_none], obj.get("valorFrete"))
        aguardarConfirmacao = from_union([from_bool, from_none], obj.get("aguardarConfirmacao"))
        optantePeloSimples = from_union([from_bool, from_none], obj.get("optantePeloSimples"))
        possuiPagtoComplementar = from_union([from_bool, from_none], obj.get("possuiPagtoComplementar"))
        pagtosComplementares = from_union([lambda x: from_list(PagtosComplementare.from_dict, x), from_none], obj.get("pagtosComplementares"))
        dadosEntrega = from_union([DadosEntrega.from_dict, from_none], obj.get("dadosEntrega"))
        enderecoCobranca = from_union([Endereco.from_dict, from_none], obj.get("enderecoCobranca"))
        valorTotalPedido = from_union([from_float, from_none], obj.get("valorTotalPedido"))
        valorTotalComplementar = from_union([from_float, from_none], obj.get("valorTotalComplementar"))
        valorTotalComplementarComJuros = from_union([from_float, from_none], obj.get("valorTotalComplementarComJuros"))
        return CriacaoPedidoReqDTO(produtos, enderecoEntrega, destinatario, campanha, cnpj, pedidoParceiro, idPedidoMktplc, senhaAtendimento, apolice, administrador, parametrosExtras, valorFrete, aguardarConfirmacao, optantePeloSimples, possuiPagtoComplementar, pagtosComplementares, dadosEntrega, enderecoCobranca, valorTotalPedido, valorTotalComplementar, valorTotalComplementarComJuros)

    def to_dict(self) -> dict:
        result: dict = {}
        result["produtos"] = from_union([lambda x: from_list(lambda x: to_class(Produto, x), x), from_none], self.produtos)
        result["enderecoEntrega"] = from_union([lambda x: to_class(Endereco, x), from_none], self.enderecoEntrega)
        result["destinatario"] = from_union([lambda x: to_class(Destinatario, x), from_none], self.destinatario)
        result["campanha"] = from_union([from_int, from_none], self.campanha)
        result["cnpj"] = from_union([from_str, from_none], self.cnpj)
        result["pedidoParceiro"] = from_union([from_int, from_none], self.pedidoParceiro)
        result["idPedidoMktplc"] = from_union([from_str, from_none], self.idPedidoMktplc)
        result["senhaAtendimento"] = from_union([from_str, from_none], self.senhaAtendimento)
        result["apolice"] = from_union([from_str, from_none], self.apolice)
        result["administrador"] = from_union([from_int, from_none], self.administrador)
        result["parametrosExtras"] = from_union([from_str, from_none], self.parametrosExtras)
        result["valorFrete"] = from_union([to_float, from_none], self.valorFrete)
        result["aguardarConfirmacao"] = from_union([from_bool, from_none], self.aguardarConfirmacao)
        result["optantePeloSimples"] = from_union([from_bool, from_none], self.optantePeloSimples)
        result["possuiPagtoComplementar"] = from_union([from_bool, from_none], self.possuiPagtoComplementar)
        result["pagtosComplementares"] = from_union([lambda x: from_list(lambda x: to_class(PagtosComplementare, x), x), from_none], self.pagtosComplementares)
        result["dadosEntrega"] = from_union([lambda x: to_class(DadosEntrega, x), from_none], self.dadosEntrega)
        result["enderecoCobranca"] = from_union([lambda x: to_class(Endereco, x), from_none], self.enderecoCobranca)
        result["valorTotalPedido"] = from_union([to_float, from_none], self.valorTotalPedido)
        result["valorTotalComplementar"] = from_union([to_float, from_none], self.valorTotalComplementar)
        result["valorTotalComplementarComJuros"] = from_union([to_float, from_none], self.valorTotalComplementarComJuros)
        return result


def CriacaoPedidoReqDTOfromdict(s: Any) -> CriacaoPedidoReqDTO:
    return CriacaoPedidoReqDTO.from_dict(s)


def CriacaoPedidoReqDTOtodict(x: CriacaoPedidoReqDTO) -> Any:
    return to_class(CriacaoPedidoReqDTO, x)
