# Lista-POO
# 📋 Sistema de Gerenciamento de Tarefas (CLI)

Aplicação desenvolvida em Python para gerenciamento de tarefas via terminal, utilizando conceitos de Programação Orientada a Objetos e padrões de projeto para organização e escalabilidade do código.

---

## 🚀 Funcionalidades

* ➕ Adicionar tarefas
* 📄 Listar tarefas
* ✅ Concluir tarefas
* ↩️ Desfazer última ação
* 🔁 Suporte a tarefas repetitivas
* 📌 Tarefas com subtarefas
* 👀 Notificação de usuários (Observer)

---

## 🛠️ Tecnologias Utilizadas

* Python
* Programação Orientada a Objetos (POO)

---

## 🧠 Conceitos e Padrões Aplicados

* **Command Pattern**

  * Encapsulamento de ações como objetos (adicionar, desfazer, concluir tarefas)

* **Observer Pattern**

  * Notificação automática de usuários quando há mudanças nas tarefas

* **Singleton Pattern**

  * Gerenciamento centralizado das tarefas com uma única instância

* **Modularização de código**

  * Separação em múltiplos arquivos (`main`, `gerenciador`, `tarefa`, etc.)

---

## 📂 Estrutura do Projeto

```id="proj123"
.
├── main.py          # Execução principal e menu
├── gerenciador.py   # Gerenciamento das tarefas (Singleton)
├── tarefa.py        # Definição das tarefas
├── command.py       # Implementação dos comandos
├── observer.py      # Sistema de observadores (usuários)
└── README.md
```

---

## ▶️ Como Executar

1. Clone o repositório:

```id="run1"
git clone https://github.com/seu-usuario/lista-poo.git
```

2. Acesse a pasta:

```id="run2"
cd lista-poo
```

3. Execute o programa:

```id="run3"
python main.py
```

---

## 📊 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de aplicar conceitos avançados de Programação Orientada a Objetos e padrões de projeto, simulando um sistema real de gerenciamento de tarefas com foco em organização, reutilização e manutenção do código.

---

## 📌 Melhorias Futuras

* 💾 Persistência de dados (arquivo ou banco de dados)
* 🖥️ Interface gráfica (GUI)
* 🔐 Sistema de autenticação de usuários
* 📊 Relatórios de produtividade

---
