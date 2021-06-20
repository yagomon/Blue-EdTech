# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas
print()

num=list()
par=list()
impar=list()

while True:
    n=int(input('Digite um número: (digite "sair" para sair): ').lower().replace("sair","0"))
    
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)


    if n == 0:
        break
    
    

print (num)
print (par)
print (impar)






