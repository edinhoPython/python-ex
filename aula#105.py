def notas(*N, sit=False):
  res = dict()

  cont_notas = 0

  maior_nota = 0
  menor_nota = 0

  media = 0
  for n1,c in enumerate(N):
    cont_notas += 1
    media += c
    if n1 == 0:
      maior_nota = c
      menor_nota = c
    if n1 != 0:
      if c > maior_nota:
        maior_nota = c
      elif c < menor_nota:
        menor_nota = c
  
  res['total'] = cont_notas
  res['maior'] = maior_nota
  res['menor'] = menor_nota
  res['media'] = media / cont_notas

  op = ''
  if sit == True:
    if res['media'] > 7:
      op = 'BOA'
    elif res['media'] > 6.0 and res['media'] < 7.0:
      op = 'RASUAVEL'
    elif res['media'] < 6.0:
      op = 'RUIM'
    
    res['situacao'] = op


  return res


resu = notas(1,5,4,7,10,6, sit=True)
print(resu)
