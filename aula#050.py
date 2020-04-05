soma = 0

for c in range(1,7):
  numero = int(input(f'numero {c}° '))
  if numero % 2 == 0:
    soma += numero

print(f'a soma de todos os numero e pares e {soma}')