menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Operação falhou ! O valor informado é inválido.")
    
    elif opcao == "1":
          valor = float(input("Informe o valor do saque: "))

          excedeu_saldo = valor > saldo
          
          excedeu_limite = valor > limite

          excedeu_saques = numero_saques >= LIMITE_SAQUE

          if excedeu_saldo:
              print("Saldo insuficiente.")
          
          elif excedeu_limite:
              print("O Valor do saque excede o limite.")

          elif excedeu_saques:
              print("Número máximo de saques excedido.")

          elif valor > 0:
              saldo -= valor
              extrato += f"saque: R$ {valor:.2f}\n"
              numero_saques += 1

          else:
              print("O valor informado é inválido.")
    
    elif opcao == "2":
        print("================ EXTRATO ================")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("================================")

    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")