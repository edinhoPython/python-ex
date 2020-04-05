num1 = int(input('um numero '))
num2 = int(input('um numero '))

while True:
  print('===' * 10)
  print('[ 1 ]somar\n[ 2 ]multiplicar\n[ 3 ]maior\n[ 4 ]novos numeros\n[ 5 ]sair')

  sair = ' '
  while sair not in('12345'):
    opcao = str(input('uma opcao: '))
    sair = opcao

  print('===' * 10)
  if opcao == '1':
    resu = num1 + num2
    print(f'a soma de {num1} e {num2} e iglau a {resu}')
  
  elif opcao == '2':
    resu = num1 * num2
    print(f'a multiplicacao de {num1} e {num2} e iglau a {resu}')

  elif opcao == '3':
    if num1 > num2:
      print(f'o maior numero e {num1}')
    
    elif num2 > num1:
      print(f'o maior numero e {num2}')
    
    else:
      print('os dois sao iglais')
      
  elif opcao == '4':
    num1 = int(input('um numero '))
    num2 = int(input('um numero '))

  else:
    break