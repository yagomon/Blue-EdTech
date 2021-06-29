# Projeto 03 – Simulador de Votação

# Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter duas funções:

# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um valor literal indicando se uma pessoa tem voto NEGADO,OPCIONAL e OBRIGATÓRIO nas eleições.

# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá da função autoriza_voto()) e o voto que é o número que a pessoa votou. Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):

# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco

# Sua função votacao() tem que calcular e mostrar:
#  O total de votos para cada candidato;
#  O total de votos nulos;
#  O total de votos em branco;
#  Qual candidato venceu a votação.

from time import sleep
from datetime import date

def autoriza_voto(ano):
    data = date.today()
    anoAtual = data.year
    
    if 18 > anoAtual-ano >= 16:
        return "Voto Opicional"
    elif anoAtual-ano >= 60:
        return "Voto Opicional"
    elif 60 > anoAtual-ano > 18:         
        return "Voto Obrigatório"
    elif anoAtual-ano < 16:         
        return "Voto Negado"
    else: 
        print ('Ano de Nascimento inválido')

def votacao(autorização,voto):
    if autorização == 'Voto Negado':
        print('\nVocê não pode votar!')
    if autorização != "Voto Negado":
        confirma= input(f"\nVocê deseja votar em {candidatos[voto][0]}?[S/N] ").upper()
        while confirma not in ['S','N']:
            confirma= input(f"Entrada inválida!\n\n Você deseja votar em {candidatos[voto][0]}?[DIGITE S PARA SIM E N PARA NÃO] ").upper()
            if confirma == 'N':
                print('Fale com o mesário para a correção do voto')
                break
            elif confirma == "S":
                    break    
        if confirma=='S':
            candidatos[voto].append(1)
    print()            
    
candidatos={1:['Jair Bolsonaro'],2:['Luiz Inácio Lula da Silva'],3:['Darth Vader'],4:['nulo'],5:['branco']} # dicionario com candidatos

# Titulo do programa
print()
print(('=-=')*14)
print("  S I M U L A D O R  D E  V O T A Ç Ã O   ")
print(('=-=')*14)
sleep(0.5)

# Início do programa
continuar='S'
while continuar == 'S':
    # Entrada do ano de nasc:
    anoNasc=input('\nDigite o seu ano de nascimento: ')
    while anoNasc.isnumeric() != True or len(anoNasc) != 4:
        anoNasc=input('Entrada inválida!\n\nDigite o seu ano de nascimento com 4 dígitos: [Apenas Números]\n ')
    anoNasc=int(anoNasc)

    # Titulo opções de voto
    sleep(0.5)
    print("\n\n----- O P Ç Õ E S    D E    V O T O : -----\n")
    sleep(0.5)

    # Imprimindo as opções de voto a partir do dicionário:
    for k,v in candidatos.items():
        print (k,v[0])
        sleep(0.5)

    print(f"\n{('-')*42}")
    print()
    sleep(0.4) 
       
    # Entrada do voto:
    voto=input(f'Digite o número do seu candidato ou das opções de voto nulo ou branco: ')
    while voto.isnumeric() != True:
        voto=input('Entrada inválida!\n\nDigite o número das opções acima para computar seu voto: ')
    while voto not in['1','2','3','4','5']:
        voto=input('Entrada inválida!\n\nDigite o número de 1 a 5, segundo as opções, para computar seu voto:')    
    voto=int(voto)

    # Testando se a pessoa pode votar e guardando a resposta na váriavel autoriza:
    autoriza= autoriza_voto(anoNasc)
   
    # Validação e adição dos votos no dicionário
    votacao(autoriza,voto)

    # Adicionar mais votos ou não:
    print(('=-=')*15)
    sleep(0.5)
    continuar= input('\nDeseja adicionar mais votos?[S/N] ').upper()
    while continuar not in ['S','N']:
        continuar= input('Entrada inválida!\n\nDigite S para continuar adicionando novos votos ou N para se não houve mais ninguém para votar?[S/N] ').upper()
    if continuar == 'N':
        break
    print()
    print(('=-=')*15)

# Titulo bonitinho kkk    
print()
print(('=-=')*15)
print("A P U R A Ç Ã O  D O S  R E S U L T A D O S   ")
print(('=-=')*15)
sleep(0.5)

# Soma dos votos:
bolsoTotal= sum(candidatos[1][1:])
lulaTotal= sum(candidatos[2][1:])
vaderTotal= sum(candidatos[3][1:])
nuloTotal= sum(candidatos[4][1:])
brancoTotal= sum(candidatos[5][1:])

# Impressões em tela finais:
print(f'\n{candidatos[1][0]} obteve {bolsoTotal} voto(s).\n')
sleep(0.5)
print(f'{candidatos[2][0]} obteve {lulaTotal} voto(s).\n')
sleep(0.5)
print(f'{candidatos[3][0]} obteve {vaderTotal} voto(s).\n')
sleep(0.5)
print(f'Houveram {nuloTotal} voto(s) {candidatos[4][0]}(s).\n')
sleep(0.5)
print(f'Houveram {brancoTotal} voto(s) em {candidatos[5][0]}.\n')

print(('=-=')*14)
print()

# Condições para saber quem ganhou:
if vaderTotal < bolsoTotal > lulaTotal and nuloTotal< bolsoTotal > brancoTotal:
    print(f'{candidatos[1][0]} venceu as Eleições!')

elif vaderTotal < lulaTotal > bolsoTotal and nuloTotal< lulaTotal > brancoTotal:
    print(f'  {candidatos[2][0]} venceu as Eleições!')

elif lulaTotal < vaderTotal > bolsoTotal and nuloTotal< vaderTotal > brancoTotal:
    print(f'  {candidatos[3][0]} venceu as Eleições!')

elif vaderTotal < nuloTotal > bolsoTotal and lulaTotal< nuloTotal > brancoTotal:
    print(f'  A maoria dos votos foram {candidatos[4][0]}s.\nAs eleições precisam ser refeitas!')

elif vaderTotal < brancoTotal > bolsoTotal and nuloTotal< brancoTotal > lulaTotal:
    print(f'  A maoria dos votos foram em {candidatos[5][0]}.\nAs eleições precisam ser refeitas!') 

print()
print(('=-=')*14)

# Ao professor:

# Não consegui manter o print dentro da função 2 pois imprimiria todos os resultados em tela ao fim de cada votação e  a intenção era imprimir os resultados somente no final. Por isso, optei por tirar os prints da função e deixa-los fora do while.

# Poderia deixar o programa mais simples utilizando contadores ao invés de listas e dicionários, mas quiz tentar utilizar todo o conteúdo aprendido até aqui. 

# Acredito que o correto seria informar que o usuário não pode votar assim que ele inserisse o ano de nascimento. Mas, na questão pede para faze-lo após a inserção do voto, então, tentei fazer conforme pede na questão.
  
