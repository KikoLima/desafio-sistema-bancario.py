menu = """
=== Seja Bem Vindo! Estou aqui para te ajudar ===

Por favor, me diga o número da opção desejada!

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("""              
             ====== Operação falhou! ======
                  
                O valor informado é inválido!
                Por favor reinicie a operação! """)

    elif opcao == "2":
        valor = float(input("Valor do saque: " ))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("""
                ====== Operação falhou! ======
                  
                Você não tem saldo suficiente.""")

        elif excedeu_limite:
            print("""
                ====== Operação falhou! ======
                  
            O Valor Máximo por sque é R$ 500.
                  
             Por favor reinicie a operação!""")

        elif excedeu_saques:
            print("""
                     ====== Operação falhou! ======
                  
                Você excedeu o limite de saques diário.""")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("""
                ====== Operação falhou! ======
                  
                  Informe um valor válido.""")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\nObrigado por ultilizar nossos terminais de auto-atendimento! ")
        print("\n==========================================")

    elif opcao == "4":
        break

    else:
        print("""
                ====== Operação falhou! ======
              
                    Digite uma opção válida.""")
