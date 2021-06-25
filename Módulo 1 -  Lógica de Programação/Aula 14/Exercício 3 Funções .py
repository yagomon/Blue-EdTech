# 3. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    custo= c
    taxaImposto=taxa/100
    return (taxaImposto*custo)+custo

c=float(input("Digite o custo da mercadoria: "))
taxa= int(input('Digite a taxa sobre as vendas'))

print(f'\nO custo com imposto sobre as vendas é {somaImposto(taxa,c)}\n')