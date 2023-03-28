from abc import ABC, abstractmethod

class Conta (ABC):
    @abstractmethod
    def __init__(self, id_conta: int, saldo: float):
        self.__id_conta = id_conta
        self.__saldo = saldo
        
    def sacar(self, valor: float):
        pass
    
    def depositar(self, valor: float):
        pass

    def get_id_conta(self) -> int:
        return self.__id_conta

    def set_id_conta(self, id_conta: int) -> None:
        self.__id_conta = id_conta

    def get_saldo(self) -> float:
        return self.__saldo

    def set_saldo(self, saldo: float) -> None:
        self.__saldo = saldo