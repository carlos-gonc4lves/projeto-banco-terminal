from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação inválida! Valor do depósito deve ser positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print("Operação inválida! O valor informado é inválido.")

        elif excedeu_saldo:
            print("Operação inválida! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação inválida! O valor do saque excedeu o limite permitido!")

        elif excedeu_saques:
            print("Operação inválida! Excedeu o número máximo de saques permitidos!")

        else:
            saldo -= valor
            numero_saques += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            extrato += f"{data_hora} - Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================\n")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
