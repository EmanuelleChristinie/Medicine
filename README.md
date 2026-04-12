# MedControl - 1.0.0

**Problema:** Dificuldade de idosos em gerenciar horários de múltiplos medicamentos.
**Solução:** Uma CLI simples para cadastrar e listar horários de remédios.
## 🚀 Funcionalidades Principais
* **Cadastro de Medicamentos:** Registro de nome, dosagem e horário.
* **Listagem Organizada:** Visualização clara de todos os remédios agendados.
* **Remoção Segura:** Exclusão de itens da lista após a conclusão do tratamento.
* **Validação de Dados:** Sistema que impede registros vazios ou entradas inválidas.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** [Python](https://www.python.org/)
* **Testes:** [Pytest](https://docs.pytest.org/)
* **Linting/Qualidade:** [Flake8](https://flake8.pycqa.org/)
* **CI/CD:** [GitHub Actions](https://github.com/features/actions)

## 📋 Requisitos de Engenharia de Software (Atendidos)
Este projeto foi construído seguindo rigorosas boas práticas de desenvolvimento moderno:
* **Versionamento Semântico:** Uso do padrão `MAJOR.MINOR.PATCH` (v1.0.0).
* **Análise Estática:** Verificação de estilo de código automatizada.
* **Integração Contínua:** Pipeline que executa testes e linter a cada `push`.
* **Documentação Estruturada:** README completo para reprodutibilidade.

## Como rodar
1. Instale as dependências: `pip install -r requirements.txt` (ou os pacotes do pyproject)
2. Execute: `python src/main.py`

## Testes e Qualidade
- Rodar testes: `pytest`
- Rodar linter: `flake8 src/`