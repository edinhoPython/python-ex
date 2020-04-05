nota_1 = float(input('primeira nota do aluno '))
nota_2 = float(input('segunda nota do aluno '))

nota_final = (nota_1 + nota_2) / 2

print(f'a media foi {nota_final}')
if nota_final > 7.0:
  print('aluno aprovado')

elif nota_final > 5.0 and nota_final < 6.9:
  print('o aluno estar de recuperacao')

else:
  print('o aluno estar reprovado')