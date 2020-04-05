resutado = {}

resutado['nome'] = str(input('Nome: '))
resutado['media'] = float(input(f'media de {resutado["nome"]} '))

print(f'nome e iglau a {resutado["nome"]}')
print(f'a media e iglau a {resutado["media"]} ')
if resutado['media'] >= 7.0:
  print('situacao e iglau a aprovado')
else:
  print('situacao e reprovado')