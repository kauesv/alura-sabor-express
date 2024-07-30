from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    def __init__(self, nome, preco, descricao):
        # Puxando os atributos do ItemCardapio
        super().__init__(nome,preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        #Subtrai 8% do preço
        self._preco -= (self._preco * 0.05)