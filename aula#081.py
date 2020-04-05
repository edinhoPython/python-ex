numeros = []
cont = 0

while True:
  numero = int(input('um numero '))
  numeros.append(numero)
  cont += 1

  continu = str(input('quer continuar [S/N] ')).upper()
  if continu == 'N':
    break

numeros.sort()
numeros.sort(reverse = True)
print(f'voce digitou {cont} elementos')
print(f'em ordem decrecente e {numeros}')
if 5 in numeros:
  print('o valor 5 faz parte da lista')
else:
  print('o valor 5 nao foi encontrado')