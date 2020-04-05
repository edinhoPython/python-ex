#guardar dados
jogador = dict()
jols = list()
total_gols = 0

#dados de cadratro
jogador['nome'] = str(input('nome do jogador '))
cont_partidas = int(input('quantas partidas jogadas '))
for c in range(1,cont_partidas + 1):
  partida = int(input(f'quantos gols na partida {c}'))
  total_gols += partida
  jols.append(partida)
jogador['gols'] = jols
jogador['total'] = total_gols

#mostrando o resultado
print('-=-'*20)
print(jogador)
print('-=-'*20)
for n,g in jogador.items():
  print(f'no campo {n} tem o valor {g}')
print('-=-'*20)
print(f'o jogador {jogador["nome"]} jogou {cont_partidas} partidas')
for c,v in enumerate(jols):
  print(f'  => na partida {c}, fez {v} gols')
print(f'foi um total de {jogador["total"]} gols')
#fim