class Avaliacao:

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 5:
            self._nota = valor
        else:
            raise ValueError('Nota deve estar entre 0 e 5.')