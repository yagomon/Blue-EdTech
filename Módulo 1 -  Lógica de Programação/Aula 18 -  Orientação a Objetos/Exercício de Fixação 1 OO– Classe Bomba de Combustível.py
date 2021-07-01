# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba

class bombaCombustível:
    def __init__(self):
        self.tipoCombustivel= ''
        self.valorLitro = 0
        self.quantidadeCombustivel = 1000

    def abastecerPorValor(self):
        valor= float(input('\nQuanto, em reais, gostaria de abastecer?\nR$'))
        litros= valor/self.valorLitro
        print(f'\nVocê abasteceu {litros:.2f} litros.')
        self.alterarQuantidadeCombustivel(litros)

    def abastecerPorLitro(self):
        litros= float(input('\nQuantos litros?\nR: '))
        preco= litros * self.valorLitro
        print(f'\nO total a pagar é R$ {preco:.2f}.')
        self.alterarQuantidadeCombustivel(litros)

    def alterarValor(self):
         if self.tipoCombustivel == '1':
             self.valorLitro = 6.07
         elif self.tipoCombustivel == '2':
             self.valorLitro = 4.97
         else:
             self.valorLitro = 4.49 

    def alterarCombustivel(self):
        print("\nBem vindo ao posto Python!\n\nDigite o número do combustível com qual deseja abastecer:")
        print('1- Gasolina')
        print('2- Etanol')
        print('3- GNV')
        tipo=input('R: ')
        self.tipoCombustivel=tipo
        self.alterarValor()

    def alterarQuantidadeCombustivel(self,litros):
        quantidade= self.quantidadeCombustivel-litros
        self.quantidadeCombustivel= quantidade
        print(f'Ainda temos {self.quantidadeCombustivel:.2f} litros na bomba.\n')

p1= bombaCombustível()

p1.alterarCombustivel()

print("\nDeseja abastecer por Preço ou por Litro?:")
print('1- Preço')
print('2- Litro')
modo=input('R: ' )

if modo == '1':
 p1.abastecerPorValor()
elif modo == '2':
    p1.abastecerPorLitro()    