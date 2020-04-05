media = 0
homen_mais_velho = ''
nome_homen = ' '
mulheres = 0

for contador in range(1,5):
  print(f'------ {contador}° pessoa ------')
  nome = str(input('nome da pessoa '))
  idade = int(input('idade '))
  sexo = str(input('sexo [M/F] ').upper())

  media += idade

  if contador == 1:
    homen_mais_velho = idade

  if idade > homen_mais_velho and sexo == 'M':
    homen_mais_velho = idade
    nome_homen = nome
  
  if idade < 20 and sexo == 'F':
    mulheres += 1

print(f'a media das idades e de {media/4}')
print(f'o homen mais velho foi {nome_homen} e a idade e {homen_mais_velho}')
print(f'foram {mulheres} mulheres menores de 20 anos')