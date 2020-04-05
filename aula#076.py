produtos = ('caderno', 15.00,'lapis', 1,'borracha', 3,'caneta',2.70,'mochila', 10.00)

print('-' * 38)
print(f"{'listagem de preços':^40}")
print('-' * 38)
for posi in range(0,len(produtos)):
  if posi % 2 == 0:
    print(f'{produtos[posi]:.<30}',end=' ')
  
  else:
    print(f'R${produtos[posi]:>5.2f}')