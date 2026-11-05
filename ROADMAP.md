# Roadmap — Python do Zero

Trilha de 9 projetos, do básico ao avançado. Cada projeto introduz conceitos novos e reaproveita os anteriores.

**Repositório:** `D:\PROJETOS\python\python-do-zero`
**Método:** uma parte por vez, com `# TODO` para preencher. O gabarito só vem no fim de cada etapa.

---

## Visão geral

| # | Projeto | Entrega | Status |
|---|---------|---------|--------|
| 1 | Calculadora interativa | `calculadora.py` | 🔄 refazendo |
| 2 | Gerenciador de tarefas | `tarefas.py` + `tarefas.json` | ⬜ |
| 3 | Conversor de moedas | `conversor.py` | ⬜ |
| 4 | Rastreador de clima | pacote com módulos | ⬜ |
| 5 | Chatbot local | `chatbot.py` + `regras.py` | ⬜ |
| 6 | CRUD com SQLite | `agenda.py` + `agenda.db` | ⬜ |
| 7 | API REST com FastAPI | `main.py` + `models.py` | ⬜ |
| 8 | Webhook receiver | `webhook.py` | ⬜ |
| 9 | SaaS mínimo | projeto completo + Docker | ⬜ |

---

## Etapa 1 — Calculadora interativa (CLI)

Pede dois números e uma operação, mostra o resultado.

**Conceitos**
- Variáveis e o significado do `=` ("recebe", não "igual")
- Tipos: `str`, `int`, `float`
- Conversão de tipos e por que o resultado precisa ser guardado
- `input()` e `print()`
- f-strings
- Condicionais: `if / elif / else`
- Indentação como delimitador de bloco
- Comparação `==` vs. atribuição `=`

**Bônus (ao final da trilha)**
- Divisão por zero
- Loop para repetir o cálculo
- Operadores `**` e `%`

---

## Etapa 2 — Gerenciador de tarefas (JSON)

Menu no terminal para adicionar, listar, concluir e remover tarefas, salvando em arquivo.

**Conceitos**
- Listas: índice, `len()`, `.append()`, `.pop()`
- Dicionários: pares chave → valor, acesso e alteração
- Lista de dicionários (a estrutura de dados mais comum do dia a dia)
- Loop `for` e `enumerate()`
- Loop `while` e o menu que repete
- Funções: `def`, parâmetros, `return`
- Leitura e escrita de arquivos com `open()` e `with`
- Módulo `json`: `load()` e `dump()`

**Bônus**
- Data de criação em cada tarefa
- Filtro por pendentes/concluídas
- Editar a descrição de uma tarefa

---

## Etapa 3 — Conversor de moedas (API pública)

Consulta a cotação do dia em uma API e converte valores.

**Conceitos**
- O que é uma API REST e o que é um endpoint
- Biblioteca `requests`: `get()`, `status_code`, `.json()`
- `requirements.txt` e instalação de dependências
- Navegação em JSON aninhado
- `try / except` para o primeiro tratamento de erros
- Separação entre buscar dados e exibir dados

---

## Etapa 4 — Rastreador de clima (API + OOP)

Consulta a previsão de uma ou mais cidades, pela linha de comando.

**Conceitos**
- Classes: `class`, `__init__`, `self`, atributos e métodos
- Objetos como "fichas" com dados e comportamento juntos
- Módulos: dividir o código em arquivos e usar `import`
- `argparse`: receber parâmetros pela linha de comando
- Exceções: hierarquia, `raise`, exceções personalizadas
- `if __name__ == "__main__"`

---

## Etapa 5 — Chatbot local (regras)

Responde a perguntas com base em um conjunto de regras, sem IA.

**Conceitos**
- Dicionários aninhados
- `match / case` (Python 3.10+)
- Métodos de string: `.lower()`, `.strip()`, `.split()`, `in`
- Módulo `logging`: níveis, formato e arquivo de log
- List comprehensions

---

## Etapa 6 — CRUD completo com SQLite

Agenda de contatos com banco de dados local.

**Conceitos**
- `sqlite3`: conexão, cursor, `execute()`, `commit()`
- CRUD: Create, Read, Update, Delete
- Queries parametrizadas e por que concatenar SQL é perigoso
- Context managers (`with`) e o protocolo por trás deles
- Decorators: funções que embrulham outras funções
- Separação em camadas: dados, regra de negócio e interface

---

## Etapa 7 — API REST com FastAPI

Transforma o CRUD da etapa anterior em uma API consumível por qualquer cliente.

**Conceitos**
- Métodos HTTP: GET, POST, PUT, DELETE e os códigos de status
- Roteamento e path/query parameters
- Pydantic: modelos e validação automática
- Type hints
- `uvicorn` e o servidor de desenvolvimento
- Documentação automática (Swagger)
- Injeção de dependências

---

## Etapa 8 — Webhook receiver (eventos do GitHub)

Recebe eventos enviados por um serviço externo e reage a eles.

**Conceitos**
- Diferença entre API (você pergunta) e webhook (ele avisa)
- Parsing de payload e headers
- Verificação HMAC: garantir que o remetente é legítimo
- `hashlib` e `hmac`
- Idempotência: por que o mesmo evento pode chegar duas vezes
- Fila de processamento e resposta rápida
- Túnel local para testes (ngrok ou similar)

---

## Etapa 9 — Projeto final: SaaS mínimo

API + webhook + banco, empacotado e testado.

**Conceitos**
- Variáveis de ambiente e `.env` (segredos fora do código)
- Docker: imagem, container, `Dockerfile`, `docker-compose`
- `pytest`: testes unitários, fixtures e mocks
- Estrutura de projeto profissional
- Migrations de banco
- Autenticação por token
- Deploy

---

## Depois da trilha

Com base no [roadmap.sh/python](https://roadmap.sh/python), o que fica para a sequência:

| Tema | Por quê |
|---|---|
| `venv`, `pip`, `poetry`/`uv` | Gestão de dependências além do básico |
| Tipagem estática (`mypy`) | Pegar erros antes de rodar |
| Programação assíncrona (`async`/`await`) | Chamadas de rede em paralelo |
| ORMs (SQLAlchemy) | Mapear tabelas para classes |
| Padrões de projeto | Soluções conhecidas para problemas recorrentes |
| Estruturas de dados e algoritmos | Base para entrevistas e para a faculdade |
| Automação e scripts | Ponte com o trabalho do dia a dia |

---

## Revisão final

Depois da Etapa 9, voltamos aos projetos 1 a 8 para implementar os bônus que ficaram pendentes. Cada um será resolvido com o repertório acumulado, o que fecha o ciclo e serve de revisão geral.
