class Conta:

    proximo_numero = 123456789

    def __init__(
        self,
        idcliente,
        agencia,
        titular,
        saldo,
        tipoconta,
        limite
    ):

        self.idcliente = idcliente
        self.idconta = Conta.proximo_numero
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo
        self.tipoconta = tipoconta
        self.limite = limite

    def transferirDinheiro(self, contaDestino, valor):

        if valor <= 0:
            return False

        if valor > self.saldo:
            return False

        self.saldo -= valor

        contaDestino.receberDinheiro(valor)

        return True


    def verificarSaldo(self):

        return self.saldo


    def receberDinheiro(self, valor):

        if valor > 0:

            self.saldo += valor


    def verificarCredito(self):

        return self.limite


    def depositarDinheiro(self, valor):

        if valor > 0:

            self.saldo += valor

            return True

        return False


    def sacarDinheiro(self, valor):

        if valor <= 0:
            return False

        # NÃO PERMITE SAQUE MAIOR QUE O SALDO

        if valor > self.saldo:
            return False

        self.saldo -= valor

        return True


    def desativarConta(self):

        self.saldo = 0

        return True