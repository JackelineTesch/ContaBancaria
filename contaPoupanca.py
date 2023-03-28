from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float = 0.0):
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento/100

    def sacar(self, valor: float) -> None:
        if self._Conta__saldo >= valor:
            self._Conta__saldo -= valor
            print("Seu saque foi realizado com sucesso. O saldo em sua Conta Poupança é de: R$", self._Conta__saldo)
        else:
            print("Saldo insuficiente!")

    def depositar(self, valor: float) -> None:
        self._Conta__saldo += valor
        print("Depósito realizado com sucesso. Seu saldo em Conta Poupança é de: R$", self._Conta__saldo)

    def verificar_rendimento(self, unidade_de_tempo: str, tempo_de_aplicacao: float) -> None:
        self.unidade_de_tempo = unidade_de_tempo
        self.tempo_de_aplicacao = tempo_de_aplicacao
        
        if unidade_de_tempo == "dias":
            tempo_de_aplicacao /= 365
        elif unidade_de_tempo == "meses":
            tempo_de_aplicacao /= 12
                    
        saldo_com_rendimento =self._Conta__saldo * (1 + self.__taxa_de_rendimento) ** tempo_de_aplicacao
        rendimento = saldo_com_rendimento - self._Conta__saldo
        print(f"Seu dinheiro renderá: R${rendimento:.2f}")
        
    def get_taxa_de_rendimento(self) -> float:
        return self.__taxa_de_rendimento

    def set_taxa_de_rendimento(self, nova_taxa: float) -> None:
        self.__taxa_de_rendimento = nova_taxa/100