# opcao = int(input('Escolha uma opção: '))

# if opcao == 1:
#     print('Você escolheu a opção 1')
# elif opcao == 2:
#     print('Você escolheu a opção 2')
# else:
#     print('Opção inválida')
    
# print('##############################')

saldo = 1000
saque = 0
conta = input('Digite o tipo da conta: ')

match conta:
    case 'corrente':
        print('Conta corrente')
        
    case 'poupanca':
        print('Conta poupança')
    
    case 'salario':
        print('Conta salário')
    
    case 'investimento':
        print('Conta investimento')
    
    case _:
        print('Conta inválida')

if conta == 'corrente':
    saque = 500
    saldo -= saque
    print(f'Saque realizado com sucesso! Saldo atual: {saldo}')
    
elif conta == 'poupanca':
    saque = 1000
    saldo -= saque
    print(f'Saque realizado com sucesso! Saldo atual: {saldo}')

elif conta == 'salario':
    saque = 1500
    saldo -= saque
    print(f'Saque realizado com sucesso! Saldo atual: {saldo}')

elif conta == 'investimento':
    saque = 2000
    saldo -= saque
    print(f'Saque realizado com sucesso! Saldo atual: {saldo}')
        
else:
    print('Conta inválida')