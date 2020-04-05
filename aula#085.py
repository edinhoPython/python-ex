numeros = [[],[]]
valor = 0

for cont in range(1,8):
  valor = int(input('um numero '))
  if valor % 2 == 0:
    numeros[0].append(valor)
  else:
    numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'os numeros pares foi {numeros[0]}')
print(f'os numeros impares foi{numeros[1]}')