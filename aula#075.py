numero1 = int(input('um numero '))
numero2 = int(input('um numero '))
numero3 = int(input('um numero '))
numero4 = int(input('um numero '))

numeros = (numero1,numero2,numero3,numero4)

print(f'voce digitou os valores {numeros}')

numeros_9 = 0
posi_3 = 0
valores_pares = [ ]

for posi in numeros:
  if posi == 9:
    numeros_9 += 1
  
  if 3 in numeros:
    posi_3 = numeros.index(3)
  
  if posi % 2 == 0:
    valores_pares.append(posi)

print(f'voce digitou o numero 9, {numeros_9} vezes')
print(f'o 3 apareceu na posicao {posi_3}')
print(f'os valores pares foi {valores_pares}')