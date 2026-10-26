from cs01conta import Conta


class ContaPoupanca(Conta):

    def __init__(
        self,
        idcliente,
        agencia,
        titular,
        cpf
    ):

        super().__init__(
            idcliente,
            agencia,
            titular,
            0.0,
            "Conta Poupança",
            0.0
        )

        self.cpf = cpf
        self.taxa_de_rendimento = 0.01

    def transferirDinheiro(self, contaDestino, valor):
        return super().transferirDinheiro(contaDestino, valor)

    def sacarDinheiro(self, valor):
        return super().sacarDinheiro(valor)

    def verificarSaldo(self):
        return super().verificarSaldo()

    def calcularRendimento(self):

        rendimento = self.saldo * 0.01

        self.saldo += rendimento

        return rendimento

    def desativarConta(self):
        super().desativarConta()