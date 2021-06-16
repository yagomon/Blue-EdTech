#3 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de acordo com o intervalo passado.

print()
ini= int(input("Digite um número para ínicio do contador: "))
fim= int(input("Digite um número para o final do contador: "))
pulo=int(input("Digite de quanto em quanto quer pular a cotagem: "))
 
for i in range(ini,fim+1,pulo):
  print(i)
