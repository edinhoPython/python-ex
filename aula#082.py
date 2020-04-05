valores = []
pares = []
impares = []

while True:
  valor = int(input('um numero'))
  valores.append(valor)

  if valor % 2 == 0:
    pares.append(valor)
  
  if valor % 2 == 1:
    impares.append(valor)

  conti = str(input('quer continuar [S/N] ')).upper()
  if conti == 'N':
    break
  
print(f'os valores digitados foram {valores}')
print(f'os valores pares foram {pares}')
print(f'os valores ímpares foram {impares}')