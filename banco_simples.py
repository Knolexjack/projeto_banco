menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    print ('Bem vindo ao seu banco!')
    opcao = input(menu)
    
    if opcao == '1':
        valor = float(input('informe o valor do deposito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            
        else:
            print('Operação falhou! o valor informado é invalido.')
            
    elif opcao == "2":
        valor = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITES_SAQUES
        
        if excedeu_saldo:
            print ('Opereção falhou! Você não tem saldo suficiente.')        
        
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
            
        elif excedeu_saques:
            print ('Operação falhou! Numero maximo de saques excedido.')
            
        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saques += 1
            
        else:
            print ('Operação falhou! O valor informado é invalido')
            
    elif opcao == '3':
        print ('\n---------- Extrato ----------')
        print ('Nao foram realizadas movimentações.' if not extrato else extrato)
        print (f'\nSaldo: R$ {saldo:.2f}')
        print ('-----------------------------')
        
    elif opcao == '0':
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')