numeros = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

valor = 0
for x in range(0,3):
  for y in range(0,3):
    valor = int(input(f'um valor [{x} {y}] '))
    if x == 0:
      numeros[x][y] = valor
    if x == 1:
      numeros[x][y] = valor
    if x == 2:
      numeros[x][y] = valor

for x in range(0,3):
  for y in range(0,3):
    print(f'[{numeros[x][y]:^5}]',end=' ')
  print()