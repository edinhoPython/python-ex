def dobro(V):
    resul = V * 2
    return resul

def metade(V):
    resul = V / 2
    return resul

def aumento(V, P):
    resul = V + (V * P) / 100
    return resul

def desconto(V, P):
    resul = V - (V * P) / 100
    return resul

def moeda(V):
    return f'R$ {V:.2f}'.replace('.', ',')