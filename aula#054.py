maior_de_idade = 0
menor_de_idade = 0

for contador in range(1,8):
  idade = int(input(f'em que ano a {contador}° nacel '))
  if 2018 - idade > 18:
    maior_de_idade += 1
  
  else:
    menor_de_idade += 1
  
print(f'são {maior_de_idade} pessoas que tem mais de 18 anos\nsão {menor_de_idade} pessoas menores de idade')