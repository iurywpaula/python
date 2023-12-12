"""
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
Todos os saques deve mser armazenados em uma variável e exibidos na operação extrato.

Operação extrato
Deve listar todos os depósitos e saques realizados na conta.
No fim da listagem, deve sr exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formado R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
"""

saldo = 0
limite_saque = 500
LIMITE_SAQUES = 3
extrato = ""
numero_saques = 0

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Opção: """


while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
    
    elif opcao == 's':
        valor = float(input('Informe o valor a ser sacado: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou. Saldo insuficiente.')
        elif excedeu_limite:
            print('Operação falhou. O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou. O limite de saques diários foi atingido.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R${valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operação falhou. O valor informado é inválido.')

    elif opcao == 'e':
        print("\n============= Extrato =============")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print('=====================================')

    elif opcao == 'q':
        print('Você saiu.')
        break

    else:
        print('Operação inválida. Por favor, tente novamente.')