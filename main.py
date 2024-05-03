# Definindo o menu de operações
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Função para realizar um depósito na conta
def depositar(valor, saldo, extrato):
    # Verifica se o valor do depósito é válido
    if valor > 0:
        # Adiciona o valor ao saldo
        saldo += valor
        # Registra o depósito no extrato
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        # Se o valor for inválido, exibe uma mensagem de erro
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar um saque na conta
def sacar(valor, saldo, extrato, numero_saques, limite_saques):
    # Verifica se o saque excede o saldo disponível
    excedeu_saldo = valor > saldo
    # Verifica se o saque excede o limite por operação
    excedeu_limite = valor > LIMITE_SAQUE
    # Verifica se o número máximo de saques diários foi atingido
    excedeu_saques = numero_saques >= limite_saques
    
    # Verifica se houve alguma condição que impeça o saque
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        # Deduz o valor do saque do saldo
        saldo -= valor
        # Registra o saque no extrato
        extrato.append(f"Saque: R$ {valor:.2f}")
        # Incrementa o contador de saques
        numero_saques += 1
    else:
        # Se o valor do saque for inválido, exibe uma mensagem de erro
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques

# Função para exibir o extrato da conta
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    # Verifica se há movimentações no extrato
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        # Exibe cada movimento registrado no extrato
        for movimento in extrato:
            print(movimento)
    # Exibe o saldo atual da conta
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Variáveis globais
saldo = 0
LIMITE_SAQUE = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa
while True:
    # Exibe o menu de operações e aguarda a escolha do usuário
    opcao = input(menu)

    # Verifica a opção escolhida pelo usuário
    if opcao == "d":
        # Realiza a operação de depósito
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        # Realiza a operação de saque
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        # Exibe o extrato da conta
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        # Finaliza o programa
        break

    else:
        # Se a opção escolhida for inválida, exibe uma mensagem de erro
        print("Operação inválida, por favor selecione novamente a operação desejada.")
