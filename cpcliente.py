class Cliente:

    autonumeracao = 1

    def __init__(self, nome, cpf, rg, telefone, endereco, renda):

        self.idcliente = Cliente.autonumeracao
        Cliente.autonumeracao += 1

        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.endereco = endereco
        self.renda = renda

    def cadastrarDados(self):
        pass

    def exibirDados(self):

        print("\n===== DADOS DO CLIENTE =====")
        print(f"ID Cliente: {self.idcliente}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"RG: {self.rg}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print(f"Renda: R$ {self.renda:.2f}")

    def criarConta(self):
        pass