from random import randint

#escolha automatica de um item
pc = randint(0,2)
items = ['pedra','papel','tesoura']
escolha = items[pc]

print('o que vc escolhe\n[ 0 ]pedra\n[ 1 ]papel\n[ 2 ]tesoura')

escolhaP = int(input('escolha '))

escolhaPP = items[escolhaP]

if escolhaPP == 'pedra' and escolha == 'tesoura':
  print('voce ganhou')

elif escolhaPP == 'papel' and escolha == 'pedra':
  print('voce ganhou')

elif escolhaPP == 'tesoura' and escolha == 'papel':
  print('voce ganhou')

elif escolhaPP == escolha:
  print('foi empate')

else:
  print('ganhei')