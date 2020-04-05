cont = 0

num1 = int(input('primeiro termo '))
razao = int(input('razao: '))

cont1 = num1
while cont < 10:
  print(f'{cont1}-> ', end=' ')
  cont1 += razao

  cont += 1
print('fim')