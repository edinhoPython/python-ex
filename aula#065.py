soma = 0
cont = 0

maior = 0
meno = 0

while True:
  numero = int(input('um numero '))

  if cont == 0:
    maior = meno = numero
  
  if cont > 0:
    if numero < meno:
      meno = numero
    if numero > maior:
      maior = numero

  soma += numero
  cont += 1

  print(maior)
  print(meno)

  continuar = str(input('quer continuar [S/N] ').upper())
  
  if continuar == 'N':
    break
  

print(f'voce digitou {cont} numeros e a media foi {soma/cont}')
print(f'o maoir numero foi {maior} e o menor foi {meno}')