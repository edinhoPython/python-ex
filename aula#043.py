pesso = float(input('qual seu peso '))
altura = float(input('qual sua altura '))

imc = pesso / (altura * altura)

print(f'seu imc e {imc:.1f}', end=" ")

if imc < 18.5:
  print('abaixo do peso')

elif imc > 18.5 and imc < 25:
  print('peso ideal')

elif imc > 25 and imc < 30:
  print('sobrepeso')

elif imc > 30 and imc < 40:
  print('obesidadde')

else:
  print('obesidade morbida')