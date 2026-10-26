from cpcliente import Cliente
from cs02contacorre import ContaCorrente
from cs03contapoupa import ContaPoupanca

clientes = {}
contas = {}
logins = {}


def criar_conta():

    print("\n===== CRIAR CONTA =====")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    renda = float(input("Renda: "))

    login = input("Crie um login: ")
    senha = input("Crie uma senha: ")

    cliente = Cliente(
        nome,
        cpf,
        rg,
        telefone,
        endereco,
        renda
    )

    print("\n1 - Conta Corrente")
    print("2 - Conta Poupança")

    tipo = input("Escolha: ")

    limite = cliente.renda * 0.30

    if tipo == "1":

        conta = ContaCorrente(
            cliente.idcliente,
            1,
            cliente.nome,
            cliente.cpf,
            limite
        )

        

    else:

        conta = ContaPoupanca(
            cliente.idcliente,
            1,
            cliente.nome,
            cliente.cpf
        )

    clientes[cliente.idcliente] = cliente
    contas[cliente.idcliente] = conta

    logins[login] = {
        "senha": senha,
        "idcliente": cliente.idcliente
    }

    print("\nConta criada com sucesso!")
    print(f"Número da Conta: {conta.idconta}")


def acessar_conta():

    login = input("Login: ")
    senha = input("Senha: ")

    if login not in logins:

        print("\nUsuário não encontrado.")
        return

    if logins[login]["senha"] != senha:

        print("\nSenha incorreta.")
        return

    idcliente = logins[login]["idcliente"]

    cliente = clientes[idcliente]
    conta = contas[idcliente]

    while True:

        print(f"\n=== BEM-VINDO {cliente.nome.upper()} ===")

        print("1 - Consultar Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Dados do Cliente")
        print("6 - Ver Limite")
        print("7 - Calcular Rendimento")
        print("8 - Dados da Conta")
        print("9 - Listar Contas")
        print("10 - Desativar Conta")
        

        op = input("\nEscolha: ")

        elif op == "1":

            print("\n===== CONSULTA DE SALDO =====")

            print(
                f"Saldo disponível: "
                f"R$ {conta.verificarSaldo():.2f}"
            )

        elif op == "2":

            print("\n===== DEPÓSITO =====")

            print("1 - Dinheiro")
            print("2 - PIX")
            print("3 - TED")

            input("Escolha: ")

            valor = float(
                input("Valor do depósito: R$ ")
            )

            if conta.depositarDinheiro(valor):

                print(
                    "\nDepósito realizado com sucesso."
                )

                print(
                    f"Saldo atualizado: "
                    f"R$ {conta.verificarSaldo():.2f}"
                )

            else:

                print("Valor inválido.")

        elif op == "3":

            print("\n===== SAQUE =====")

            valor = float(
                input("Valor do saque: R$ ")
            )

            if conta.sacarDinheiro(valor):

                print("\nSaque realizado.")

                print(
                    f"Saldo restante: "
                    f"R$ {conta.verificarSaldo():.2f}"
                )

            else:

                print(
                    "\nSaldo insuficiente."
                )

        elif op == "4":

            print("\n===== TRANSFERÊNCIA =====")

            cpf_destino = input(
                "CPF destinatário: "
            )

            valor = float(
                input("Valor: R$ ")
            )

            conta_destino = None

            for conta_temp in contas.values():

                if conta_temp.cpf == cpf_destino:

                    conta_destino = conta_temp
                    break

            if conta_destino is None:

                print(
                    "Conta não encontrada."
                )

                continue

            if conta.transferirDinheiro(
                conta_destino,
                valor
            ):

                print(
                    "\nTransferência realizada."
                )

                print(
                    f"Saldo restante: "
                    f"R$ {conta.verificarSaldo():.2f}"
                )

            else:

                print(
                    "\nSaldo insuficiente."
                )
        elif op == "5":

            print("\n===== DADOS DO CLIENTE =====")

            print(
                f"ID Cliente: {cliente.idcliente}"
            )

            print(
                f"Nome: {cliente.nome}"
            )

            print(
                f"CPF: {cliente.cpf}"
            )

            print(
                f"RG: {cliente.rg}"
            )

            print(
                f"Telefone: {cliente.telefone}"
            )

            print(
                f"Endereço: {cliente.endereco}"
            )

            print(
                f"Renda: "
                f"R$ {cliente.renda:.2f}"
            )
        elif op == "6":

            print("\n===== LIMITE =====")

            print(
                f"Limite disponível: "
                f"R$ {conta.verificarCredito():.2f}"
            )

        elif op == "7":

            if isinstance(
                conta,
                ContaPoupanca
            ):

                rendimento = (
                    conta.calcularRendimento()
                )

                print(
                    "\nRendimento aplicado."
                )

                print(
                    f"Valor ganho: "
                    f"R$ {rendimento:.2f}"
                )

                print(
                    f"Saldo atual: "
                    f"R$ {conta.verificarSaldo():.2f}"
                )

            else:

                print(
                    "\nSomente Conta "
                    "Poupança possui rendimento."
                )
        elif op == "8":

            print("\n===== DADOS DA CONTA =====")

            print(
                f"Titular: {cliente.nome}"
            )

            print(
                f"CPF: {cliente.cpf}"
            )

            print("Agência: 0001")

            print("Conta: 12345678-9")

            print(
                f"Tipo: {conta.tipoconta}"
            )

            print(
                f"Saldo: "
                f"R$ {conta.saldo:.2f}"
            )

            print(
                f"Limite: "
                f"R$ {conta.limite:.2f}"
            )
        elif op == "9":

            print(
                "\n===== CONTAS CADASTRADAS ====="
            )

            if len(contas) == 0:

                print(
                    "Nenhuma conta cadastrada."
                )

            else:

                for conta_temp in contas.values():

                    print()

                    print(
                        f"CPF: {conta_temp.cpf}"
                    )

                    print(
                        f"Titular: "
                        f"{conta_temp.titular}"
                    )

                    print(
                        f"Tipo: "
                        f"{conta_temp.tipoconta}"
                    )

                    print(
                        f"Saldo: "
                        f"R$ {conta_temp.saldo:.2f}"
                    )

                    print("-" * 30)
        elif op == "10":

            confirma = input(
                "\nDeseja excluir a conta? "
                "(S/N): "
            )

            if confirma.upper() == "S":

                del clientes[idcliente]
                del contas[idcliente]
                del logins[login]

                print(
                    "\nConta excluída "
                    "com sucesso."
                )

                break


def main():

    while True:

        print("\n===== BANCO =====")
        print("1 - Criar Conta")
        print("2 - Acessar Conta")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":

            criar_conta()

        elif op == "2":

            acessar_conta()

        elif op == "0":

            print("\nSistema encerrado.")
            break

        else:

            print("\nOpção inválida.")


if __name__ == "__main__":
    main()