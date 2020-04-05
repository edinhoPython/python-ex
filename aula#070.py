print('==='*10)
print('         loja baratao')
print('==='*10)

total = 0
mais_M = 0
mais_B = ' '
precoB = 0
cont = 0

while True:
  nome_pro = str(input('nome do produto '))
  preco = float(input('preço '))
  continu = str(input('quer continuar [S/N] ')).upper() [0]

  total += preco

  if preco >= 1000:
    mais_M += 1
  
  if cont == 0:
    mais_B = nome_pro
    precoB = preco
    cont = 1
  
  if preco < precoB:
    precoB = preco

  if continu == 'N':
    break

print(f'a soma dos produtos e {total}')
print(f'foram {mais_M} produtos que custa mais de R$1000')
print(f'o produto mais barato foi {mais_B}')