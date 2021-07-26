from lib.api.campanhaApi import CampanhaApi
from lib.api.formapagamentoApi import FormaPagamentoApi
from lib.api.pedidoApi import PedidoApi
from lib.api.produtoApi import ProdutoApi
from lib.api.segurancaApi import SegurancaApi
from lib.models.request.PedidoCarrinhoDTO import PedidoCarrinhoDTO
from lib.models.request.ConfirmacaoReqDTO import ConfirmacaoReqDTO
from lib.models.request.CriacaoPedidoReqDTO import CriacaoPedidoReqDTO


## CAMPANHA API
def get_campanha(dt_inicio: str, dt_fim: str):
    return CampanhaApi().getcampanhas(dt_inicio, dt_fim)


def get_forma_pagamento_campanha(id_campanha: str, cnpj: str):
    return CampanhaApi().getformaspagamento(id_campanha, cnpj)


## FORMA DE PAGAMENTO API
def get_opcoes_parcelamento(id_forma_pagamento: str, id_campanha: str, cnpj: str, valor_parcelar: str):
    return FormaPagamentoApi().getopcoesparcelamento(id_forma_pagamento, id_campanha, cnpj, valor_parcelar)


## PEDIDO API
def post_calcular_carrinho(pedido: PedidoCarrinhoDTO):
    return PedidoApi().postcalcularcarrinho(pedido)


def get_dados_pedido_parceiro(id_compra: str, cnpj: str, id_campanha: str, id_pedidoparceiro: str,
                              id_pedidomktplc: str):
    return PedidoApi().getdadospedidoparceiro(id_compra, cnpj, id_campanha, id_pedidoparceiro, id_pedidomktplc)


def patch_pedidos_cancelamento_ou_confirmacao(id_compra: str, confirmacao: ConfirmacaoReqDTO):
    return PedidoApi().patchpedidoscancelamentoconfirmacao(id_compra, confirmacao)


def get_nota_fiscal_pedido(id_compra: str, id_compraentrega: str, formato: str):
    return PedidoApi().getNotaFiscalPedido(id_compra, id_compraentrega, formato)


def post_criar_pedido(pedido: CriacaoPedidoReqDTO):
    return PedidoApi().postCriarPedido(pedido)


## PRODUTO API
def get_dados_produto(id_logista: str, id_sku: str):
    return ProdutoApi().getdadosproduto(id_logista, id_sku)


def get_lista_dadosproduto(id_logista: str, id_sku: []):
    return ProdutoApi().getlistadadosproduto(id_logista, id_sku)


def get_dados_produtocampanha(id_campanha: str, id_sku: str, id_lojista: str, cnpj: str):
    return ProdutoApi().getdadosprodutocampanha(id_campanha, id_sku, id_lojista, cnpj)


## SEGURANCA API
def getchave():
    return SegurancaApi().getchave()
