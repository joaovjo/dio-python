saldo = 500.0

def sacar(valor: float) -> None:
    global saldo
    if saldo >= valor:
        saldo -= valor
        print(f'Saque de R$ {valor} realizado com sucesso.')
        print(f'Saldo atual: R$ {saldo}')
        
sacar(float(100))