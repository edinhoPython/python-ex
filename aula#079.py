numeros = []

while True:
  numero = int(input('me diga um numero '))

  if numero not in numeros:
    print('adicionado com suceso')
    numeros.append(numero)
  
  else:
    print('o valor e duplicado nao vou adicionar')
  
  s_n = str(input('quer continuar [S/N] ')).upper()

  if s_n == 'N':
    break

final = sorted(numeros)
print(f'voce digitou os valores {final}')