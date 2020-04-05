total = 0
cont = 0

while True:
  numero = int(input('um numero ? [999 para parar] '))
  if numero != 999:
    total += numero
    cont += 1
  
  else:
    break
print(f'voce digitou {cont} a soma de todos os valores e {total}')