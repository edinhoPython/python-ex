numeros = []
for c in range(1,6):
  numero = int(input('um numero '))

  if numeros == [ ]:
    print(f'numero {numero} foi adicionado')
    numeros.append(numero)
  
  elif numero < numeros[0]:
    print(f'o numero {numero} foi adicionado na posicao 0')
    numeros.append(numero)

  else:
    print(f'o numero {numero} foi adicionado na posicao 1')
    numeros.insert(1,numero)

ordenada = sorted(numeros)
print(ordenada)