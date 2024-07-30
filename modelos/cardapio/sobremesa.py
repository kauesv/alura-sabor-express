from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        #Subtrai 15% do preço
        self._preco -= (self._preco * 0.15)