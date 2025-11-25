from tarefa import TarefaSimples, TarefaRepetitiva, TarefaComSubtarefas
from command import AdicionarTarefaCommand, DesfazerCommand, ConcluirTarefaCommand
from gerenciador import GerenciadorDeTarefas
from observer import Usuario


def menu():
    print("\n📋 MENU DE TAREFAS:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Desfazer última ação")
    print("5. Sair")


def main():
    ger = GerenciadorDeTarefas.get_instancia()
    usuario = Usuario("Theo")
    ger.adicionar_observador(usuario)

    while True:
        menu()
        opcao = input("Escolha: ")

       
        if opcao == "1":

            print("\n🟦 ADICIONAR TAREFA")
            print("Digite 0 a qualquer momento para voltar.\n")

            print("Tipos: 1) Simples  2) Repetitiva  3) Com Subtarefas")
            tipo = input("Escolha o tipo: ")

            if tipo == "0":
                continue

            if tipo not in ["1", "2", "3"]:
                print("⚠️ Tipo inválido!")
                continue

            titulo = input("Título da tarefa: ")
            if titulo == "0":
                continue

            desc = input("Descrição: ")
            if desc == "0":
                continue

            
            prazo = input("Prazo (dd/mm/aaaa) (deixe vazio para nenhum): ")
            if prazo == "0":
                continue
            if prazo.strip() == "":
                prazo = None

            
            if tipo == "1":
                tarefa = TarefaSimples(titulo, desc, prazo)

            elif tipo == "2":
                tarefa = TarefaRepetitiva(titulo, desc, prazo)

            elif tipo == "3":
                tarefa = TarefaComSubtarefas(titulo, desc, prazo)
                qtd = input("Quantas subtarefas adicionar? ")

                if qtd == "0":
                    continue

                try:
                    qtd = int(qtd)
                except:
                    print("⚠️ Número inválido!")
                    continue

                for _ in range(qtd):

                    sub_titulo = input("Título da subtarefa: ")
                    if sub_titulo == "0":
                        continue

                    sub_desc = input("Descrição da subtarefa: ")
                    if sub_desc == "0":
                        continue

                    sub_prazo = input("Prazo da subtarefa (vazio = nenhum): ")
                    if sub_prazo == "0":
                        continue
                    if sub_prazo.strip() == "":
                        sub_prazo = None

                    tarefa.adicionar_subtarefa(
                        TarefaSimples(sub_titulo, sub_desc, sub_prazo)
                    )

            cmd = AdicionarTarefaCommand(ger, tarefa)
            cmd.executar()
            print("✔️ Tarefa adicionada com sucesso!")

     
        elif opcao == "2":
            print("\n🗂️ LISTA DE TAREFAS:")
            if not ger.tarefas:
                print("Nenhuma tarefa cadastrada.")
                continue

            for i, t in enumerate(ger.tarefas, start=1):
                t.exibir_detalhes(i)

                if hasattr(t, "subtarefas"):
                    for j, s in enumerate(t.subtarefas, start=1):
                        print(f"   {i}.{j} ", end="")
                        s.exibir_detalhes()

      
        elif opcao == "3":
            print("\n🟦 CONCLUIR TAREFA")

            if not ger.tarefas:
                print("⚠️ Nenhuma tarefa cadastrada!")
                continue

            print("\nEscolha o número da tarefa para concluir:\n")

            for i, t in enumerate(ger.tarefas, start=1):
                status = "(✔️ concluída)" if t.concluida else ""
                print(f"{i}. {t.titulo} {status}")

                if hasattr(t, "subtarefas"):
                    for j, s in enumerate(t.subtarefas, start=1):
                        status_s = "(✔️ concluída)" if s.concluida else ""
                        print(f"   {i}.{j} {s.titulo} {status_s}")

            print("\nDigite 0 para voltar.")
            escolha = input("Número: ")

            if escolha == "0":
                continue

            
            if "." in escolha:
                try:
                    parte_t, parte_s = escolha.split(".")
                    idx_t = int(parte_t) - 1
                    idx_s = int(parte_s) - 1

                    tarefa = ger.tarefas[idx_t]
                    subtarefa = tarefa.subtarefas[idx_s]

                    cmd = ConcluirTarefaCommand(ger, subtarefa)
                    cmd.executar()

                except:
                    print("⚠️ Número inválido!")
                continue

            
            try:
                idx = int(escolha) - 1
                if 0 <= idx < len(ger.tarefas):
                    tarefa = ger.tarefas[idx]
                    cmd = ConcluirTarefaCommand(ger, tarefa)
                    cmd.executar()
                else:
                    print("⚠️ Número inválido!")
            except:
                print("⚠️ Entrada inválida!")


        elif opcao == "4":
            cmd = DesfazerCommand(ger)
            cmd.executar()

        elif opcao == "5":
            print("👋 Saindo do sistema...")
            break

        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    main()
