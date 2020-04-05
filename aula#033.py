num1 = int(input("um numero "))
num2 = int(input("um numero "))
num3 = int(input("um numero "))

maior = num1
menor = num1

if num2 > maior:
  maior = num2

if num2 < menor:
  menor = num2

if num3 > maior:
  maior = num1

if num3 < menor:
  menor = num3

print(f"o maior numero digitado foi {maior}")
print(f"o menor numero digitado foi {menor}")
