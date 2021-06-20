### Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pstotal=[]
ptotal=[]

for i in range(2):
    ps= input('Qual seu nome? ').capitalize()
    p= float (input('Digite seu peso: ').replace("," , "."))
    pstotal.append(ps)
    ptotal.append(p)

imax= ptotal.index(max(ptotal))
imin= ptotal.index(min(ptotal))

print()

print(f'{pstotal[imax]} tem o maior peso, {max(ptotal)} kg.')
print(f'{pstotal[imin]} tem o menor peso, {min(ptotal)} kg.')