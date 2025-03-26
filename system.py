import time

contas = {}

def criar_conta():
    '''Cria uma nova conta bancária.'''
    cpf = input('Digite seu CPF(Somente números): ')
    if cpf in contas:
        print('Erro: CPF já cadastrado!')
        return
    time.sleep(1)
    nome = input('Digite seu nome: ')
    time.sleep(1)

    saldo = float(input('Digite o saldo inicial: R$ '))
    time.sleep(1)
    contas[cpf] = {
        'nome': nome,
        'saldo': saldo,
        'extrato': []
    }
    time.sleep(1)

    print('Conta criada com sucesso!')

def depositar():
    '''Realiza um depósito na conta.'''
    cpf = input('Digite seu CPF: ')
    if cpf not in contas:
        print('Erro: conta não encontrada!')
        return
    time.sleep(1)

    valor = float(input('Digite o valor do depósito: R$ '))
    if valor > 0:
        contas[cpf]['saldo'] += valor
        contas[cpf]['extrato'].append(f'Depósito: +R$ {valor:.2f}')
        print(f'Depósito realizado! Saldo atual: R$ {contas[cpf]["saldo"]:.2f}')
    else:
        print('Erro: Valor inválido!')
    time.sleep(1)

def sacar():
    '''Realiza um saque da conta.'''
    cpf = input('Digite seu CPF: ')
    if cpf not in contas:
        print('Erro: Conta não encontrada!')
        return
    time.sleep(1)

    valor = float(input('Digite o valor do saque: R$ '))
    if 0 < valor <= contas[cpf]['saldo']:
        contas[cpf]['saldo'] -= valor
        contas[cpf]['extrato'].append(f'Saque: -R$ {valor:.2f}')
        print(f'Saque realizado! Saldo atual: R$ {contas[cpf]["saldo"]:.2f}')
    else:
        print('Saldo insuficiente ou valor inválido!')
    time.sleep(1)

def transferir():
    '''Realiza uma trasnferência entre contas.'''
    cpf_origem = input('Digite o CPF: ')
    if cpf_origem not in contas:
        print('Erro: Conta de origem não encontrada!')
        return
    time.sleep(1)

    cpf_destino = input('Digite o CPF do destinatário: ')
    if cpf_destino in contas:
        print('Erro: Conta de destino não encontrada!')
        return
    time.sleep(1)

    valor = float(input('Digite o valor da trasnferência: R$ '))
    if 0 < valor <= contas[cpf_origem]['saldo']:
        contas[cpf_origem]['saldo'] -= valor
        contas[cpf_destino]['saldo'] += valor
        contas[cpf_origem]['extrato'].append(f'Transferência enviada: -R$ {valor:.2f} para {contas[cpf_destino]["nome"]}')
        contas[cpf_destino]['extrato'].append(f'Transferência recebida: +R$ {valor:.2f} de {contas[cpf_origem]['nome']}')
        print('Transferência realizada com sucesso!')
    else:
        print('Erro: Saldo insuficiente ou valor inválido')
    time.sleep(1)

def extrato():
    '''Exibe o extrato da conta.'''
    cpf = input('Digite o CPF: ')
    if cpf not in contas:
        print('Erro: conta não encontrada!')
        return
    time.sleep(1)
    print('\n=== Extrato Bancário ===')

    for operacao in contas[cpf]['extrato']:
        print(operacao)
    print(f'Saldo atual: R$ {contas[cpf]['saldo']:.2f}')
    print('=========================')

def menu():
    '''Exibe o menu principal e gerencia as opções.'''
    while True:
        print('\n=== Banco Digital ===')
        time.sleep(0.4)
        print('1. Criar Conta')
        time.sleep(0.4)
        print('2. Depositar')
        time.sleep(0.4)
        print('3. Sacar')
        time.sleep(0.4)
        print('4. Transferir')
        time.sleep(0.4)
        print('5. Extrato')
        time.sleep(0.4)
        print('6. Sair')
        time.sleep(0.4)
        opcao = input('Escolha um opção: ')
        time.sleep(0.4)

        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            depositar()
        elif opcao == '3':
            sacar()
        elif opcao == '4':
            transferir()
        elif opcao == '5':
            extrato()
        elif opcao == '6':
            print('Obrigado por usar o Banco Digital Ferreira! Saindo...')
            time.sleep(1)
            break
        else:
            print('Opção invalida! tente novamente.')
menu()