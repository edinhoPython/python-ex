print('{:=^40}'.format('lojas edinho'))

preco = float(input('qual o valor da compra '))

print('voce vai pagar de que formar\n[ 1 ]dinheiro/chekc\n[ 2 ]avista no cartao\n[ 3 ]2X no cartao\n[ 4 ]3X no cartao\n')

forma_pag = int(input('qual a forma de pagamento '))

if forma_pag == 1:
  total = preco - (preco * 10 / 100)
  print(f'oque custava {preco} vai custar {total}')

elif forma_pag == 2:
  total = preco - (preco * 5 / 100)
  print(f'oque custava {preco} vai custar {total}')

elif forma_pag == 3:
  print(f'oque custava {preco} vai custar {preco}')

else:
  total = preco + (preco * 20 / 100)
  print(f'oque custava {preco} vai custar {total}')