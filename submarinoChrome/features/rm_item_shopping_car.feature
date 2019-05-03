#language: pt

Funcionalidade: Remover item de carrinho de compras
    Cenário: Remover item no carrinho de compras
        Dado um item adicionado no Carrinho
        Quando removo este item
        Então uma solicitação será enviada
        