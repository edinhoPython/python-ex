from random import randint

numero = randint(0,10)
erros = 0

print('olá, sou seu computador pensei em um numero tente adivinhar')
while True:
  resposta = int(input('um numero entre 0 e 10. '))
  print('==='* 5)

  if resposta < numero:
    print(f'maior que {resposta}')
    erros += 1
  
  elif resposta > numero:
    print(f'menor que {resposta}')
    erros += 1

  else:
    print('voce acertou, parabens')
    print(f'voce acertou em {erros} tentativas')
    break
  print('==='* 5)