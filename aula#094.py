#guardar dados
pessoas_total = []
pessoas_cont = 0
media_idade = 0
feminino_nomes = []

#coletar dados
while True:
  pessoas = {}
  #dados das pessoas
  pessoas['nome'] = str(input('Nome: '))
  idade = int(input('Idade: '))

  pessoas['idade'] = idade
  pessoas['sexo'] = str(input('Sexo [M/F] '))[0]

  if pessoas['sexo'] == 'f':
    feminino_nomes.append(pessoas['nome'])

  pessoas_cont += 1
  media_idade += idade
  pessoas_total.append(pessoas)
  #condição de saida
  conti = str(input('continuar ')).upper() [0]
  if conti == 'N':
    break

#saida (ezibindo os dados)
media_idade = media_idade / pessoas_cont
print(f'foram {pessoas_cont} pessoas cadastrada')
print(f'a media das idade e de {media_idade:.0f}')
print('nome de todas as mulhelheres e de ',end='')
for nome in feminino_nomes:
  print(nome,end='')