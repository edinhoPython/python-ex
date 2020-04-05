maior_peso = 0
menor_peso = 0

for contador in range(1,6):
  peso = float(input(f'peso da {contador}° pessoa'))
  if contador == 1:
    maior_peso = peso
    menor_peso = peso
  
  if peso > maior_peso:
    maior_peso = peso
  
  if peso < menor_peso:
    menor_peso = peso

print(f'o maior peso foi {maior_peso}\no menor peso foi {menor_peso}')