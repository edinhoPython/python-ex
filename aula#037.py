numero = int(input("um numero inteiro "))
print("[ 1 ] binario \n[ 2 ] octal \n[ 3 ] hexadecimal")
escola = int(input("quer converter em que "))
if escola == 1:
  print(f"o numero {numero} em binario e {bin(numero)[2:]}")
if escola == 2:
  print(f"o numero {numero} convertido para octal e {oct(numero)[2:]}")
if escola == 3:
  print(f"o numero {numero} convertido em hexadecimal e {hex(numero)[2:]}")

