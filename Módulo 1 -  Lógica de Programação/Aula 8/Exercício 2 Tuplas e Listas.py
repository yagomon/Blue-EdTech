# 2- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

print()
r1 = int (input("Você telefonou para a vítima? [SIM / NÃO] ").upper().replace("SIM","1").replace("NÃO","0"))
r2 = int (input("Você esteve no local do crime? [SIM / NÃO] ").upper().replace("SIM","1").replace("NÃO","0"))
r3 = int (input("Você mora perto da vítima? [SIM / NÃO] ").upper().replace("SIM","1").replace("NÃO","0"))
r4 = int (input("Você devia para a vítima? [SIM / NÃO] ").upper().replace("SIM","1").replace("NÃO","0"))
r5 = int (input("Você já trabalhou com a vítima? [SIM / NÃO] ").upper().replace("SIM","1").replace("NÃO","0"))

resps=[r1,r2,r3,r4,r5]
sim= sum(resps)

if sim == 2:
  print("\nVocê é Você é Suspeito\n")
elif sim == 3  or sim == 4:
  print ("\nVocê é Cúmplice\n")
elif  sim >= 5:
  print ("\nVocê é o Assassino\n")
else:
  print("\nVocê é Inocente\n")