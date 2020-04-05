while True:
  numero = int(input('um numero para ver sua tabuada '))
  if numero >= 0:
    print('==='* 5)
    for cont in range(1,11):
      print('{} X {:2} = {}'.format(numero, cont, numero * cont))
    print('==='* 5)
  else:
    break