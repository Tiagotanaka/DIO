def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    # Operação Saque
    valor = float(input("Digite o valor do Saque: "))
    
    if numero_saques == limite_saques:
        print ("Não foi possivel realizar o saque, pois ja execedeu o limite de saques diário. Retornando ao menu.")
        return saldo, extrato, numero_saques

    elif valor > limite:
        print(f"Não foi possivel realizar o saque, valor desejado maior que o limite de valor por saque.\nLimite valor diario: R${limite}.\nRetornando ao menu.")
        return saldo, extrato, numero_saques
    
    elif valor > saldo:
        print(f"Não foi possivel realizar o saque, valor desejado maior que o saldo disponivel.\nSaldo atual: R${saldo}.\nRetornando ao menu.")
        return saldo, extrato, numero_saques

    elif valor <= 0:
        print("Valor informado invalido.\nRetornando ao menu.")
        return saldo, extrato, numero_saques
    
    saldo -= valor
    extrato += f"Saque de: R${valor:.2f}\n"
    print(f"Saque de R${valor:.2f} efutuado com sucesso!")
    numero_saques+=1
    return saldo, extrato, numero_saques

def deposito(saldo, extrato,/):
    # Operação Deposito
    valor = float(input("Digite o valor do deposito: "))
    if valor <= 0:
        print (f"Não foi possivel efutuar o deposito, valor informado é invalido. Retornando ao menu.\n")
        return saldo, extrato
    saldo += valor
    extrato += f"Deposito de: R${valor:.2f}\n"
    print(f"Deposito de R${valor:.2f} efutuado com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    # Operação Extrato
    print("=========== EXTRATO ===========")
    if "Deposito" in extrato or "Saque" in extrato:
        print (f"{extrato}\nSaldo disponivel: R${saldo:.2f}.")
    else:
        print(f"Não foram realizadas movimentações.\n\nSaldo disponivel: R${saldo:.2f}.")
    print("===============================")

def verifica_cpf(cpf, usuarios):
    # Verifica se existem mais usuarios com o mesmo cpf
    verifica_cpf = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return verifica_cpf[0] if verifica_cpf else None

def criar_usuario(usuarios):
    # Operação cria usuarios
    cpf = input("Digite o CPF: ")
    verificacao = verifica_cpf(cpf, usuarios)
    if verificacao:
        print("Usuario ja existente com o mesmo usuario. Retornando ao menu.")
        return
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento(dd/mm/aaaa): ")
    logradouro = input("Digite o logradouro: ")
    numero_casa = input("Digite o numero da casa: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    sigla_estado = input("Digite a sigla do estado: ")
    endereco = logradouro + ", " + numero_casa + " - " + bairro + " - " + cidade + " - " + sigla_estado
    usuarios.append({"nome":nome, "data":data_nascimento, "cpf":cpf, "endereco":endereco})
    print("Usuario criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    # Operação cria conta
    cpf = input("Informe seu CPF do usuario:")
    verificacao = verifica_cpf(cpf, usuarios)
    if verificacao:
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta+1, "verificacao":verificacao}

    print("Usuario não encontrado. Retornando ao menu.")

def listar_usuarios(usuarios):
    # Operação lista os usuarios
    for usuario in usuarios:
        print(f"""
=============================================
Nome: {usuario["nome"]}
Data de nascimento: {usuario["data"]}
CPF: {usuario["cpf"]}
Endereço: {usuario["endereco"]}
=============================================""")

def listar_contas(contas):
    # Operação lista as contas
    for conta in contas:
        print(f"""
=============================================
Agencia: {conta["agencia"]}
Numero da conta: {conta["numero_conta"]}
Titular: {conta["verificacao"]["nome"]}
=============================================""")
        

menu = """
---------- Menu ----------
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuario
[5] Listar usuarios
[6] Criar conta
[7] Listar contas
[0] Sair

►"""
contas = []
usuarios = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == "1":
        # Operação de deposito
        saldo, extrato = deposito(saldo,extrato)

    elif opcao == "2":
        # Operação de saque
        saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "3":
        # Operação de extrato
        exibir_extrato(saldo,extrato=extrato)

    elif opcao == "4":
        # Operação de criar usuario
        criar_usuario(usuarios)

    elif opcao == "5":
        # Operação de Listar usuarios
        listar_usuarios(usuarios)

    elif opcao == "6":
        # Operação de criar conta
        teste = len(contas)
        conta = criar_conta(AGENCIA, teste, usuarios)
        
        if conta:
            contas.append(conta)

    elif opcao == "7":
        # Operação de listar contas
        listar_contas(contas)

    elif opcao == "0":
        #Sair
        print("Finalizado as operações.")
        break

    else: 
        print ("Operação inválida, por favor selecione novamente a operação desejada.")

    