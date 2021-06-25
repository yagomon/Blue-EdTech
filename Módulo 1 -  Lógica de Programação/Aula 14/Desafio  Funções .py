# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.


import datetime

print()

def dataConvert(d,m,a):
    try:
        newDate = datetime.datetime(a,m,d)
        m=str(m)
        if m == "1":  
            m= "janeiro"
        elif m == "2":
            m= "fevereiro"
        elif m == "3":
            m= "março"
        elif m == "4":
            m= "abril"
        elif m == "5":
            m= "maio"
        elif m == "6":
            m = "junho"
        elif m == "7":
            m= "julho"
        elif m == "8":
            m= "agosto"
        elif m == "9":
            m= "setembro"
        elif m == "10":
            m= "outubro"
        elif m == "11":
            m= "novembro"
        elif m == "12":
            m= "dezembro"    
        return f'{d} de {m} de {a}' 
    except ValueError:
        return 'NULL'

    



data=input('Digite uma data [DD/MM/AAAA]: ')

l= data.split('/')

print()


dia= int(l[0])
mes= int(l[1])
ano= int(l[2])


print(dataConvert(dia,mes,ano))



