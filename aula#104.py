def leiaInt(msg):
  ok = False
  valor = 0
  while True:
    n1 = input(msg)
    if n1.isnumeric():
      ok = True
      valor = n1
    else:
      print('\033[31mdigite um valor valido\033[m')
    if ok == True:
      break
  return valor


n = leiaInt('digite um numero ')
print(f'voce digitou o numero {n}')