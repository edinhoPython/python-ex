from ex112.utilidadeCeV import moeda

def leia_valor():
    while True:
        num = input('um numero ')

        if num.isalpha() or num.isspace() or num == '':
            print('invalido')

        if num.isnumeric():
            num = float(num)
            moeda.resulmo(num)
            break

        if ',' in num:
            num = num.replace(',', '.')
            num = float(num)
            moeda.resulmo(num)
            break
