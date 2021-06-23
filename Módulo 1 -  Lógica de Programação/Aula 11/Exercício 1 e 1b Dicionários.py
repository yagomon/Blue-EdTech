#### 2 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.

# l=[1, 4, 5, 6, 7, 9]

# d=dict()

# for i in l:
#     d[i]=i**2

# print (d)


#### b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​

print()

d=dict()
for i in range(10):  # ou for i in range(1,11)
    d[i+1]= (i+1)**2 #        d[i]= (i)**2

print(d)    






