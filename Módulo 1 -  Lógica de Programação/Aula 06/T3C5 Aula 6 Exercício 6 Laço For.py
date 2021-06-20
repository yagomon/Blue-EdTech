# 6 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

f= input("Digite uma frase: ")

for i in f:
    if i in "aeiouáàâéêíóôAEIOUÁÀÂÉÊÍÓÔ":
        f= f.replace(i,"")

print (f)         


