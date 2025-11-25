
from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def executar(self):
        pass

    @abstractmethod
    def desfazer(self):
        pass



class AdicionarTarefaCommand(Comando):
    def __init__(self, gerenciador, tarefa):
        self.gerenciador = gerenciador
        self.tarefa = tarefa

    def executar(self):
        self.gerenciador.adicionar_tarefa(self.tarefa)
        self.gerenciador.historico.append(self)

    def desfazer(self):
        self.gerenciador.remover_tarefa(self.tarefa)



class ConcluirTarefaCommand(Comando):
    def __init__(self, gerenciador, tarefa):
        self.gerenciador = gerenciador
        self.tarefa = tarefa
        self.antes_concluida = tarefa.concluida

    def executar(self):
        self.tarefa.concluir()
        self.gerenciador.notificar(f"Tarefa '{self.tarefa.titulo}' concluída!")
        self.gerenciador.historico.append(self)

    def desfazer(self):
        if not self.antes_concluida:
            self.tarefa.reabrir()
            self.gerenciador.notificar(f"Desfazer: Tarefa '{self.tarefa.titulo}' reaberta.")



class DesfazerCommand(Comando):
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def executar(self):
        if self.gerenciador.historico:
            comando = self.gerenciador.historico.pop()
            comando.desfazer()
        else:
            print(" Nenhuma ação para desfazer.")

    def desfazer(self):
        pass  
