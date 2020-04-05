numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','katorze','quinze','dizseis','diszsete','dissoito','disznove','vinte')

while True:
  numero = int(input('digite um numero entre 0 e 20 '))

  if numero > 20:
    print('tente novamente',end=' ')
  
  if numero <= 20:
    print(numeros[numero])
    break