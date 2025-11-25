
from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        """Método chamado quando há uma notificação."""
        pass


class Usuario(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f" Notificação para {self.nome}: {mensagem}")
