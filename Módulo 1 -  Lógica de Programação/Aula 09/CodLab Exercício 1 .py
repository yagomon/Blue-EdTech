#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    pergunta=int(input('Digite um Valor: '))
    if pergunta not in numeros:
        numeros.append(pergunta)
        print('Numero Adcionado!')    
    
    else:
        print('Valor Duplicado, Digite outro')


    resposta= input('Deseja imprimir os numeros ou quer continuar? [I- Imprimir / C- Continuar]: ')
    while resposta not in 'IiCc':
        resposta= input('Entrada inválida!\nDeseja imprimir os numeros ou quer continuar? [I- Imprimir / C- Continuar]: ')
    if resposta in 'Ii':
         break
print(sorted(numeros))