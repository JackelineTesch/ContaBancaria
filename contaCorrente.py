from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self.__limite = limite

    def sacar(self, valor: float) -> None:
        try:
            if self.get_saldo() + self.__limite >= valor:
                self._Conta__saldo -= valor
                print("Seu saque foi realizado com sucesso. O saldo em sua Conta Corrente é de: R$", self._Conta__saldo)
            else:
                raise ValueError ("Saldo insuficiente!")
        except ValueError as ve:
            print(ve)

    def depositar(self, valor: float) -> None:
        self._Conta__saldo += valor
        print("Depósito realizado com sucesso. Seu saldo em Conta Corrente é de: R$", self._Conta__saldo)
        
    def get_limite(self) -> float:
        return self.__limite

    def set_limite(self, limite: float) -> None:
        self.__limite = limite
