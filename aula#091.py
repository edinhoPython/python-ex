from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)}
for c,n in jogo.items():
  print(f'o {c} tirou {n}')
  sleep(1)
print('-=-'*10)
raking = []
raking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(raking):
  print(f'{i+1}° lugar {v[0]} com {v[1]}')
  sleep(1)