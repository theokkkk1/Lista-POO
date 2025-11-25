
from tarefa import Tarefa
from observer import Observador

class GerenciadorDeTarefas:
    _instancia = None

    def __init__(self):
        self.tarefas = []
        self.historico = []
        self.observadores = []

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = GerenciadorDeTarefas()
        return cls._instancia

  
    def adicionar_observador(self, observador: Observador):
        self.observadores.append(observador)

    def notificar(self, mensagem: str):
        for obs in self.observadores:
            obs.atualizar(mensagem)

  
    def adicionar_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)
        self.notificar(f"Tarefa '{tarefa.titulo}' adicionada!")

    def concluir_tarefa(self, tarefa: Tarefa):
        tarefa.concluir()
        self.notificar(f"Tarefa '{tarefa.titulo}' foi concluída!")

    def remover_tarefa(self, tarefa: Tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            self.notificar(f"Tarefa '{tarefa.titulo}' foi removida!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, t in enumerate(self.tarefas, start=1):
                t.exibir_detalhes(i)
                if hasattr(t, "subtarefas") and t.subtarefas:
                    for j, s in enumerate(t.subtarefas, start=1):
                        s.exibir_detalhes(f"{i}.{j}")
