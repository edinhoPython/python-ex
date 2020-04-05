primeiro = int(input('primeiro termo da PA '))
razao = int(input('razão '))

decimo = primeiro + (11 -1) * razao

for cont in range(primeiro,decimo,razao):
  print(f'{cont}',end="-> ")
print('acabou')