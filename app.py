from modelos.restaurante import Restaurante

restaurante_a = Restaurante('a', 'comida')
restaurante_a.alternar_estado()
restaurante_a.receber_avaliacao('Marcella', 5)
restaurante_a.receber_avaliacao('Marcy', 2)
restaurante_a.receber_avaliacao('itsMarcyy', 1.5)

restaurante_b = Restaurante('b', 'bebida')
restaurante_c = Restaurante('c', 'sobremesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()