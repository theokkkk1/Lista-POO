
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, prazo=None):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False
        self.prazo = prazo

    def concluir(self):
        self.concluida = True
        print(f" Tarefa concluída: {self.titulo}")

    def reabrir(self):
        self.concluida = False
        print(f" Tarefa reaberta: {self.titulo}")

    def exibir_detalhes(self, numero=None):
        status = " Concluída" if self.concluida else "⏳ Pendente"
        prefixo = f"{numero}. " if numero is not None else ""
        print(f"\n {prefixo}{self.titulo} — {status}")
        print(f"   Descrição: {self.descricao}")
        print(f"   Prazo: {self.prazo if self.prazo else '(não definido)'}")


class TarefaSimples(Tarefa):
    pass


class TarefaRepetitiva(Tarefa):
    def __init__(self, titulo, descricao, prazo=None, intervalo="Diário"):
        super().__init__(titulo, descricao, prazo)
        self.intervalo = intervalo

    def exibir_detalhes(self, numero=None):
        super().exibir_detalhes(numero)
        print(f"   Intervalo: {self.intervalo}")


class TarefaComSubtarefas(Tarefa):
    def __init__(self, titulo, descricao, prazo=None):
        super().__init__(titulo, descricao, prazo)
        self.subtarefas = []

    def adicionar_subtarefa(self, subtarefa):
        self.subtarefas.append(subtarefa)

    def concluir(self):
        pendentes = [st for st in self.subtarefas if not st.concluida]
        if pendentes:
            print(" Não é possível concluir a tarefa principal. Existem subtarefas pendentes.")
            return
        self.concluida = True
        print(f"✔️ Tarefa principal concluída: {self.titulo}")

    def exibir_detalhes(self, numero=None):
        super().exibir_detalhes(numero)
        if not self.subtarefas:
            print("   (Sem subtarefas)")
        else:
            print("   Subtarefas:")
            for i, st in enumerate(self.subtarefas, start=1):
                status = "✔️" if st.concluida else "⏳"
                print(f"      {numero}.{i} — {st.titulo} ({status})")



class TarefaFactory:
    @staticmethod
    def criar_tarefa(tipo, titulo, descricao, prazo=None, intervalo="Diário"):
        if tipo == "simples":
            return TarefaSimples(titulo, descricao, prazo)
        elif tipo == "repetitiva":
            return TarefaRepetitiva(titulo, descricao, prazo, intervalo)
        elif tipo == "subtarefas":
            return TarefaComSubtarefas(titulo, descricao, prazo)
        else:
            raise ValueError("Tipo de tarefa inválido")
