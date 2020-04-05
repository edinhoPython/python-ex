from random import randint

numero_pc = randint(0, 5)
print('ola sou seu computador vol pensar em um numero de 0 ate 5 tente adivinhar')

numero_ps = int(input('um numero de 0 a 5 '))

if numero_ps == numero_pc:
  print('PARABENS, voce acertou')

else:
  print('voce errou tente novamente')

print(numero_pc)