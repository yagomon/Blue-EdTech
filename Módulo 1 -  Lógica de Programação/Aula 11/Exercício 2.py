### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.


estoque={'arroz':10 , 'feijão':0, 'alho':5, 'batata':2}
comprados=dict()

while True:
    
    produto= input("\nO que você deseja comprar? ").lower() # Entrada nome do produto
    
    # Quando tem o produto mas o estoque está zerado:
    while estoque.get(produto) == 0:
                
        proceed= input("\n'Produto Indisponível no momento!\n\nDeseja adquirir outro produto? ").lower() #Usuario quer escolher outro?
        if proceed=='sim':
            produto= input("\nO que você deseja comprar? ").lower() # Se sim o que?
        elif proceed == 'não': 
            exit()                 # se não encerra o programa

        while proceed not in ['sim','não']: # teste de entrada do Proceed para n quebrar o programa
            proceed= input("Entrada inválida!\n\nDigite SIM para adquirir outro produto ou NÃO para sair: ").lower().replace('nao','não')
            if proceed=='sim':
                produto= input("\nO que você deseja comprar? ").lower()
            elif proceed == 'não':
                exit()    
    
    # Quando entrada do usuario não existe no estoque:
    while produto not in estoque.keys():
        
        proceed= input("Produto Inválido!\n\nDeseja adquirir outro produto? ").lower()
        
        if proceed=='sim':
            produto= input("\nO que você deseja comprar? ").lower()
            while estoque.get(produto) == 0:
                print ('Produto Indisponível no momento!')
                proceed= input("\nDeseja adquirir outro produto? ").lower()
        elif proceed == 'não':
            exit()
        
        # Teste do proceed para não quebar o programa
        while proceed not in ['sim','não']:
            proceed= input("Entrada inválida!\n\nDigite SIM para adquirir outro produto ou NÃO para sair: ").lower().replace('nao','não')
            if proceed=='sim':
                produto= input("\nO que você deseja comprar? ").lower()
                while estoque.get(produto) == 0:
                    print ('Produto Indisponível no momento!')
                    proceed= input("\nDeseja adquirir outro produto? ").lower()
            elif proceed == 'não':
                exit() 

    # Entrada quantidade de produtos
    quant= input(f"Qual a quantidade de {produto} que deseja adquirir?: ")
    
    while quant.isnumeric() != True:
        quant= input("Entrada Inválida!\n\nQual quantidade de {produto} deseja? [Digite apenas números]: ")
    quant= int(quant)

    
    if estoque.get(produto) < quant:
        print(f'Quantidade solicitada não disponível\n\nNo momento temos {estoque.get(produto)} {produto}(s) disponivel.')

        proceed=input('\nDeseja inserir outra quantidade? ')
        while proceed not in ['sim','não']:
            proceed= input("Entrada inválida!\n\nDigite SIM para informar uma quantidade válida ou NÃO para continuar comprando: ").lower().replace('nao','não')
        if proceed=='sim':
            quant= input(f"\nDigite a nova quantidade de {produto} que deseja comprar: ").lower()
            while quant.isnumeric() != True:
                quant= input("Entrada Inválida!\n\nQual quantidade de {produto} deseja? [Digite apenas números]: ")
            quant= int(quant)
            

    estoque[produto]=estoque[produto]-quant
    comprados[produto]= quant
    
    proceed= input('\nDeseja adquirir outros itens? ').lower()
    while proceed not in ['sim','não']:
            proceed= input("Entrada inválida!\n\nDigite SIM para continuar comprando ou Não para encerrar a compra: ").lower().replace('nao','não')
    if proceed == 'não':
        break

soma_itens=0
for i in comprados.values():
    soma_itens += i

print(f'\nVocê comprou {len(comprados)} poduto(s) totalizando {(soma_itens)} itens:')

for k,v in comprados.items():
    print((f'\n{k} - {v} itens').title())