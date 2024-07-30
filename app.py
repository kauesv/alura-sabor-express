from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

def main():

    restaurante_praca = Restaurante('Praça', 'Gourmet')
    bebida_suco = Bebida("Suco de Melancia", 5.00, "Grande")
    bebida_suco.aplicar_desconto()

    prato_pao = Prato("Pão", 2.00, "O melhor pão da cidade")
    prato_pao.aplicar_desconto()

    restaurante_praca.adicionar_no_cardapio(bebida_suco)
    restaurante_praca.adicionar_no_cardapio(prato_pao)

    restaurante_praca.exibir_cardapio


# Valida se é o arquivo principal
if __name__ == '__main__':
    main()