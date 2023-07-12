menu = """Escolha a operação desejada

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)

    if opcao == "1":
        # Operação Deposito
        entrada = float(input("Digite o valor do deposito: "))
        if entrada <= 0:
            print (f"Não foi possivel efutuar o deposito, valor informado é invalido. Retornando ao menu.\n")
            continue
        saldo += entrada
        extrato += f"Deposito de: R${entrada:.2f}\n"
        print(f"Deposito de R${entrada:.2f} efutuado com sucesso!\n")

    elif opcao == "2":
        # Operação Saque
        entrada = float(input("Digite o valor do Saque: "))
        
        if numero_saques == LIMITE_SAQUES:
            print ("Não foi possivel realizar o saque, pois ja execedeu o limite de saques diário. Retornando ao menu.\n")
            continue

        elif entrada > limite:
            print(f"Não foi possivel realizar o saque, valor desejado maior que o limite de valor por saque.\nLimite valor diario: R${limite}.\nRetornando ao menu.\n")
            continue
        
        elif entrada > saldo:
            print(f"Não foi possivel realizar o saque, valor desejado maior que o saldo disponivel.\nSaldo atual: R${saldo}.\nRetornando ao menu.\n")
            continue

        elif entrada <= 0:
            print("Valor informado invalido.\nRetornando ao menu.\n")
            continue

        saldo -= entrada
        extrato += f"Saque de: R${entrada:.2f}\n"
        print(f"Saque de R${entrada:.2f} efutuado com sucesso!\n")
        numero_saques +=1

    elif opcao == "3":
        # Operação Extrato
        print("=========== EXTRATO ===========")
        if "Deposito" in extrato or "Saque" in extrato:
            print (f"{extrato}\nSaldo disponivel: R${saldo:.2f}.")
        else:
            print(f"Não foram realizadas movimentações.\n\nSaldo disponivel: R${saldo:.2f}.")
        print("===============================\n")

    elif opcao == "0":
        #Sair
        print("Finalizado as operações.")
        break

    else: 
        print ("Operação inválida, por favor selecione novamente a operação desejada.")

    