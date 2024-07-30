from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):
        # Puxando os atributos do ItemCardapio
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        #Subtrai 5% do preço
        self._preco -= (self._preco * 0.08)