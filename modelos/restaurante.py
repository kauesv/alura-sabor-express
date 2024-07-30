from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._avaliacoes = []
        self._ativo = False
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        try:
            nova_avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(nova_avaliacao)
        except ValueError as e:
            print(e)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacoes:
            return "-"
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            quantidade_de_notas = len(self._avaliacoes)

            return round(soma_das_notas / quantidade_de_notas, 1)
        
    def adicionar_no_cardapio(self, item):
        # Valida se o item for uma instancia da classe ItemCardapio ou uma derivada
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        # ele retorna o index da lista e o numero para cada item
        for index, item in enumerate(self._cardapio, start=1):
            #Valida se encontra um atributo em um objeto
            if hasattr(item, '_descricao'):
                print(f"{index}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(25)} | Descrição: {item._descricao}")
            else:
                print(f"{index}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(25)} | Tamanho: {item._tamanho}")
