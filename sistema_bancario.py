def menu ():
  menu = '''
  menu = --- MENU ---
  [1] Depositar \n
  [2] Sacar \n 
  [3] Extrato \n
  [9] Nova conta\n
  [8] Mostrar contas \n
  [7] Novo usuario \n
  [0] Sair
  
  '''
  return input(menu)


def depositar (saldo, valor, extrato,/):
  if valor > 0:
    saldo += valor
    extrato += f'Deposito R$ {valor:.2f}'
    print ('Deposito realizado com sucesso')
  else:
    print ('Informe um valor valido')
  return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_de_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_de_saques >= limite_saques
  
  if excedeu_saldo:
    print ('Falhou, saldo insuficiente ')
  elif excedeu_limite:
    print ('Falhou, o valor do saque excedeu o limite')
  elif excedeu_saques:
    print ('Falhou, excedeu numero de saques')

  elif valor > 0:
    saldo -= valor
    extrato += f'Saque R$ {valor:.2f}'
    numero_de_saques += 1 
    print ('Sucesso, saque sendo realizado')
    
  else:
    print ('Falhou, valor inválido')
    
  return saldo, extrato

def exibir_extrato (saldo, / , *, extrato):
  print ('Sem movimentações realizadas' if not extrato else extrato)
  print (f'Saldo R$ {saldo:.2f}')
  
def criar_usuario (usuarios):
  cpf = input ('Informe o cpf (somente numeros): ')
  usuario = filtrar_usuario (cpf, usuarios)
  
  if usuario:
    print ('já existe cliente com esse cpf')
    
  nome = input ('informe o nome completo: ')
  data_de_nascimento = input ('informe a data de nascimento (dia-mes-ano): ')
  endereco = input ('informe o endereço (rua - bairro - estado): ')
  
  usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereco': endereco})
  print ('usuario criado com sucesso')

def filtrar_usuario (cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
  return usuarios_filtrados [0] if usuarios_filtrados else None
 
def criar_conta (agencia, numero_conta, usuarios):
  cpf = input ('informe o cpf:')
  usuario = filtrar_usuario (cpf, usuarios)
  
  if usuario:
    print ('conta criada com sucesso')
    return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
  print ('usuario não encontrado, nao foi possivel criar conta')
  
def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência:\n{conta['agencia']}
            C/C:\n{conta['numero_conta']}
            Titular:\n{conta['usuario']['nome']}
        '''
        print("=" * 100)
        print((linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '7':
            criar_usuario(usuarios)

        elif opcao == '9':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '8':
            listar_contas(contas)

        elif opcao == '0':
            break

        else:
            print('opcao invalida')


main()