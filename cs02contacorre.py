from cs01conta import Conta


class ContaCorrente(Conta):

    def __init__(
        self,
        idcliente,
        agencia,
        titular,
        cpf,
        limite
    ):

        super().__init__(
            idcliente,
            agencia,
            titular,
            0.0,
            "Conta Corrente",
            limite
        )

        self.cpf = cpf

    def transferirDinheiro(self, contaDestino, valor):
        return super().transferirDinheiro(contaDestino, valor)

    def verificarSaldo(self):
        return super().verificarSaldo()

    def receberDinheiro(self, valor):
        super().receberDinheiro(valor)

    def verificarCredito(self):
        return super().verificarCredito()

    def depositarDinheiro(self, valor):
        super().depositarDinheiro(valor)

    def sacarDinheiro(self, valor):
        return super().sacarDinheiro(valor)

    def desativarConta(self):
        super().desativarConta()