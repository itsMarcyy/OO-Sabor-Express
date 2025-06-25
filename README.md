# POO Sabor Express

Sistema de gerenciamento de restaurantes, usando Programação Orientada a Objetos (POO) em Python. 
Projeto desenvolvido como prática do curso da Alura.

---

## Observações importantes 📌

- **Classes:** nomes começam com letra maiúscula (ex: `Restaurante`).
- **Atributos protegidos:** iniciados com `_` para indicar acesso restrito.
- **Métodos especiais (dunder methods):** como `__init__` (construtor) e `__str__` (representação em texto).
- **Decorador `@property`:** permite acessar métodos como se fossem atributos.
- **Método de classe (`@classmethod`):** atua sobre a classe como um todo.
- **Importações:** uso de `from` e `import` para organizar o código em múltiplos arquivos.

---

## 📁 Estrutura do projeto

- `modelos/avaliacao.py`: classe `Avaliacao` que representa avaliações feitas por clientes.
- `modelos/restaurante.py`: classe `Restaurante` com nome, categoria, status e avaliações.
- `main.py`: cria restaurantes, recebe avaliações e lista os dados no terminal.

---

Projeto simples com foco didático para praticar os fundamentos da Programação Orientada a Objetos com Python.
