valor_casa = float(input("qual o valor da casa "))
salario = float(input("qual o valor do seu salario "))
anos = int(input("em quntos anos deseja financiar "))

prestacao = valor_casa / (anos * 12)

minimo = salario / 30 * 100
print(f"para pagar uma casa que custa {valor_casa} vai pagar durante {anos}meses", end=" ")
print(f"a prestacao sera de {prestacao:.2f}R$")
if prestacao <= minimo:
  print(f"emprestimo pode ser concedidio")
else:
  print("emprestiomo negado")