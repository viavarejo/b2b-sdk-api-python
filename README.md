

# SDK Python para API B2B

Provê os componentes para o uso da API B2B, disponibilizado pela VIA, facilitando a integração com as documentações relacionadas:

| Swagger |
| ------ | 
| http://api-integracao-pontofrio.hlg-b2b.net/swagger/ui/index#/ |
| http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#/| 
| http://api-integracao-extra.hlg-b2b.net/swagger/ui/index#/ |

## Configurando o SDK
 Dentro da pasta [lib/utils] se encontra a classe responsavel pelas requisições (rest.py), a qual deve ser configurado duas propriedades: 
 - baseurl  (end-point utilizado).
 - token (token de acesso).
 
## APIs Disponíveis

A pasta [lib/api] contem os arquivos:
* campanhaApi.py
* formapagamentoApi.py
* pedidoApi.py
* produtoApi.py
* segurancaApi.py

Estas compõe a camada de acesso para os serviços disponibilizados pelo B2B, alguns exemplos de como utiliza-lá estão disponíveis nos testes unitarios

A seguir, são apresentadas as APIs e exemplos com as as principais operações do B2B.

- ## Campanha
    Api Utilizada para operações de campanha
    ## Obtém todas as campanhas vinculadas ao parceiro: 
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#/Campanha/Campanha_ListarCampanhaAsync 
    - http://api-integracao-pontofrio.hlg-b2b.net/swagger/ui/index#/Campanha/Campanha_ListarCampanhaAsync 
    - http://api-integracao-extra.hlg-b2b.net/swagger/ui/index#/Campanha/Campanha_ListarCampanhaAsync 

    ```python
	    from lib.api import campanhaApi
	    dto = campanhaApi.CampanhaApi().getcampanhas('2019-08-04', '2100-08-04')
    ```
    
	***
    
    ## Obtém todas as opções de pagamento para uma determinada campanha: 
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Campanha/Campanha_ListarOpcoesParcelamentoAsync |
    - http://api-integracao-pontofrio.hlg-b2b.net/swagger/ui/index#/Campanha/Campanha_ListarOpcoesParcelamentoAsync |
    - http://api-integracao-extra.hlg-b2b.net/swagger/ui/index#/Campanha/Campanha_ListarOpcoesParcelamentoAsync |
    
    ```python
    from lib.api import campanhaApi
    dto = campanhaApi.CampanhaApi().getformaspagamento('5940', '57.822.975/0001-12')
    ```
    
***

- ## Pedido
    Api utilizada para operações de pedidos
     ## Calcular carrinho:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_CalcularCarrinhoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_CalcularCarrinhoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_CalcularCarrinhoAsync
	
        ```python
	     from lib.api import pedidoApi
        produto = lib.models.request.PedidoCarrinhoDTO.Produto()
        produto.codigo = self.id_sku_criacao_pedido
        produto.quantidade = 1
        produto.idLojista = self.id_lojista

        pedidocarrinho = PedidoCarrinhoDTO()
        pedidocarrinho.idCampanha = "id_campanha"
        pedidocarrinho.cnpj = "cnpj"
        pedidocarrinho.cep = "cep"
        pedidocarrinho.produtos = [produto]
        dto = pedidoApi.PedidoApi().postcalcularcarrinho(pedidocarrinho)
        ```
		
     ## Obter os dados de pedido do parceiro:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterPedidoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterPedidoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterPedidoAsync
	
        ```python
        from lib.api import pedidoApi
        dto = pedidoApi.PedidoApi().getdadospedidoparceiro(idcompra= str(self.pedidoHelper.idPedido),
                                                   cnpj=self.cnpj,
                                                   idcampanha=str(self.id_campanha),
                                                   idpedidoparceiro=str(self.pedidoHelper.idPedidoParceiro),
                                                   idpedidomktplc=None)
        ```
		
     ## Confirma ou cancela pedidos pendentes de confirmação:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ConfirmarPedidoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ConfirmarPedidoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ConfirmarPedidoAsync
	
        ```python
        from lib.api import pedidoApi
		    confirmacao = ConfirmacaoReqDTO()
        confirmacao.idCampanha = self.id_campanha
        confirmacao.idPedidoParceiro = self.pedidocom_cartao_helper.idPedidoParceiro
        confirmacao.confirmado = True
      
        dto = pedidoApi.PedidoApi().patchpedidoscancelamentoconfirmacao(str(self.pedidocom_cartao_helper.idPedido), confirmacao)
        ```
		
     ## Obter nota fiscal do pedido:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterNFeAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterNFeAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterNFeAsync
	
        ```python
        from lib.api import pedidoApi
		    dto = pedidoApi.PedidoApi().getNotaFiscalPedido(idcompra='247473612',
                                                        idcompraentrega='91712686',
                                                        formato='PDF')
		
        ```
		
     ## Criar pedido:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterNFeAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterNFeAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Pedido/Pedido_ObterNFeAsync
	
        ```python
      from lib.api import pedidoApi
		    request_dto = CriacaoPedidoReqDTO()
        produto = lib.models.request.CriacaoPedidoReqDTO.Produto()
        enderecoEntrega = Endereco()
        destinatario = Destinatario()
        dadosEntrega = DadosEntrega()

        produto.idLojista = self.id_lojista
        produto.codigo = self.pedidoHelper.idSku
        produto.quantidade = 1
        produto.precoVenda = self.pedidoHelper.precoVenda
        produto.premio = 0

        enderecoEntrega.cep = '01525-000'
        enderecoEntrega.estado = 'SP'
        enderecoEntrega.logradouro = 'rua da se'
        enderecoEntrega.cidade = 'São Paulo'
        enderecoEntrega.numero = 63
        enderecoEntrega.referencia = 'teste'
        enderecoEntrega.bairro = 'bairro se'
        enderecoEntrega.complemento = 'teste'
        enderecoEntrega.telefone = '22333333'
        enderecoEntrega.telefone2 = '22333335'
        enderecoEntrega.telefone3 = '22333336'

        destinatario.nome = 'teste'
        destinatario.cpfCnpj = self.cpf_destinatario
        destinatario.email = 'teste@teste.com'

        dadosEntrega.valorFrete = self.pedidoHelper.valorFrete

        request_dto.produtos = [produto]
        request_dto.enderecoEntrega = enderecoEntrega
        request_dto.destinatario = destinatario
        request_dto.dadosEntrega = dadosEntrega
        request_dto.campanha = self.id_campanha
        request_dto.cnpj = self.cnpj
        request_dto.pedidoParceiro = self.gera_id_pedido_parceiro()
        request_dto.valorFrete = self.pedidoHelper.valorFrete
        request_dto.aguardarConfirmacao = True
        request_dto.optantePeloSimples = True
      
        dto = pedidoApi.PedidoApi().postCriarPedido(request_dto)
		
        ```
		
		
    
- ## Forma de Pagamento
    Api Utilizada para operações de forma de pagamento
     ## Obter opções de parcelamento:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/FormaPagamento/FormaPagamento_ListarOpcoesParcelamentoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/FormaPagamento/FormaPagamento_ListarOpcoesParcelamentoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/FormaPagamento/FormaPagamento_ListarOpcoesParcelamentoAsync
        ```python
        from lib.api import formapagamentoApi
        dto = formapagamentoApi.FormaPagamentoApi().getopcoesparcelamento("1", "5940", "57.822.975/0001-12", "1000")
        ```
- ## Produto
    Api Utilizada para operações de produto
     ## Obter dados do produto:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ObterProdutoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ObterProdutoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ObterProdutoAsync
        ```python
        from lib.api import produtoApi
        dto = produtoApi.ProdutoApi().getdadosproduto('15', '5880205')
        ```
     ## Obter lista de dados dos produtos:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ListarProdutoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ListarProdutoAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ListarProdutoAsync
        ```python
        from lib.api import produtoApi
        dto = produtoApi.ProdutoApi().getlistadadosproduto('15', ['5880205', '5880206'])
        ```
     ## Obter dados do produto por Campanha:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ObterProdutoPorCampanhaAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ObterProdutoPorCampanhaAsync
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Produto/Produto_ObterProdutoPorCampanhaAsync
        ```python
        from lib.api import produtoApi
        dto = produtoApi.ProdutoApi().getdadosprodutocampanha('5940', '5880205', '15', '57.822.975/0001-12')
        ```
- ## Seguranca
    Api Utilizada para operações de seguranca
     ## Obter chave pública 2048 bits utilizada para criptografia dos dados do cartão:
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Seguranca/Seguranca_ObterChave
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Seguranca/Seguranca_ObterChave
    - http://api-integracao-casasbahia.hlg-b2b.net/swagger/ui/index#!/Seguranca/Seguranca_ObterChave
        ```python
        from lib.api import segurancaApi
        dto = segurancaApi.SegurancaApi().getchave()
        ```
       
        
        