salario = float(input("digite o salario do funcionario "))
if salario > 1250:
  novo = salario + (salario * 10 / 100)
  print(f"com o aumento de 10% vai ser {novo:.2f}")

elif salario <= 1250:
  novo = salario + (salario * 15 / 100)
  print(f"com o aumento de 15% vai ser {novo:.2f}")