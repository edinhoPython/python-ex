total = 0

while True:
  numero = int(input('um numero ? [999 para parar] '))
  if numero != 999:
    total += numero
  
  else:
    break
print(f'a soma de todos os valores e {total}')