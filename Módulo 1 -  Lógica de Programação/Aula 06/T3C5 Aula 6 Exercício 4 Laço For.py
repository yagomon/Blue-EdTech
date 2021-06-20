####Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a soma deles (o usuário vai dizer quantos números serão informados antes de começar)

'''print()
quant= int(input('Quanto números deseja somar? '))

cont=0
nums=[]

while cont != quant:
  cont+=1
  num=int(input(f'Digite o {cont}º número? '))
  nums.append(num)

print(f'A soma de {nums} é {sum(nums)}')'''

# sem lista
'''print()
quant= int(input('Quanto números deseja somar? '))
print()

cont=0
soma=0

while cont != quant:
  cont+=1
  num=int(input(f'Digite o {cont}º número? '))
  soma+= num
print()

print(f'A soma dos números informados é {soma}.')
print()'''

# com for

'''print()
quant= int(input('Quanto números deseja somar? '))

soma=0

for i in range (quant):
  num=int(input(f'Digite o {i
  +1}º número? '))
  soma += num

print(f'A soma dos números informados é {soma}.')

print()'''

# com for e lista
print()
quant= int(input('Quanto números deseja somar? '))

nums=[]

for i in range (quant):
  num=int(input(f'Digite o {i+1}º número? '))
  nums.append(num)

print(f'A soma de {nums} é {sum(nums)}')

print()