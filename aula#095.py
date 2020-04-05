time = list()
while True:
  jogador = dict()
  jogador['nome'] = str(input('Nome: '))
  partidas = int(input('quantas partidas jogadas '))
  gols = list()
  total = 0
  for c in range(1,partidas + 1):
    partida = int(input(f'quantos gols na partida {c}: '))
    gols.append(partida)
    total += partida
  jogador['gols'] = gols
  jogador['total'] = total
  time.append(jogador)

  sair = str(input('sair S/N: ')).upper()[0]
  if sair == 'S':
    break

print('---'* 11)
for c,n in enumerate(time):
  print(f'{c:>3} ',end='')
  for c1 in n.values():
    print(f'{str(c1):<15}',end='')
  print()

while True:
  busca = int(input('dados de qual jogador [999] parar '))
  if busca == 999:
    break
  elif busca >= len(time):
    print('o cadigo {busca} nao existe, temte novamente')
  else:
    print(f'levantamento do jogador {time[busca]["nome"]}')
    for i, g in enumerate(time[busca]["gols"]):
      print(f'no jogo {i+1} fez {g} gols')
    print('-' * 40)
print('volte sempre')