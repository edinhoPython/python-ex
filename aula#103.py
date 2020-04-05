def ficha(nome='',gols=''):
  if nome == '':
    nome = '<desconhecido>'
  if gols == '':
    gols = '0'
  
  return 'o jogador ' + nome + ' fez ' + gols + ' no canpeonato'

nom = str(input('nome do jogador '))
gol = str(input('gols do jogador '))

print(ficha(nom,gol))