simbolos = []

expresao = str(input('uma exprecao '))

for letra in expresao:
  if letra == '(' or letra == ')':
    simbolos.append(letra)
NFP = 0
nap = 0

for letraF in simbolos:
  if letraF == '(':
    nap += 1
  if letraF == ')':
    NFP += 1

if nap == NFP:
  print(f'{expresao} e valida')

else:
  print('expresao invalida')