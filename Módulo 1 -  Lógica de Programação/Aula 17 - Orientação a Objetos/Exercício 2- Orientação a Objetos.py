# Vamos aprimorar o código:  cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula 14. Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador. 

class campeonato:



jogador = dict()    
golsCampeonato = 0

partidas = int(input("Quantas partidas foram jogadas? "))
for i in range(partidas):
    jogador[i+1] = int(input(f"Quantos gols foram feitos na partida {i+1}? "))
    golsCampeonato += jogador[i+1]

print(jogador)
print(golsCampeonato)