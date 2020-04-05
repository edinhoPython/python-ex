velocidade = int(input('velocidade do carro: '))

if velocidade <= 80:
    print('\033[33m' + 'tenha um bom dia ! dirija com segurança' + '\033[0;0m')

elif velocidade > 80:
    print('\033[31m' + 'MULTADO voce exedeu o limite, permitido e de 80k/h' + '\033[0;0m')
    valor = (velocidade - 80) * 7.00
    valor = str(valor)
    print('\033[31m' + 'voce vai pagar um valor de ' + '\033[0;0m',end='')
    print('\033[33m' + f'{valor}' + '\033[0;0m')
    print('\033[33m' + 'tenha um bom dia ! dirija com segurança' + '\033[0;0m')