# 💊 MedControl — Gestão de Medicamentos para Idosos

[![Python CI](https://github.com/EmanuelleChristinie/Medicine/actions/workflows/ci.yml/badge.svg)](https://github.com/EmanuelleChristinie/Medicine/actions)

**Versão:** 1.0.0

## 🎯 Sobre o Projeto

- **O Problema (Dor Real):** A dificuldade de idosos e cuidadores no gerenciamento de múltiplas medicações diárias. O esquecimento ou a confusão de horários é um problema crítico que compromete tratamentos de saúde e causa ansiedade em famílias.
- **A Solução:** O **MedControl** é uma aplicação de linha de comando (CLI) simples e direta que permite cadastrar medicamentos com suas respectivas dosagens e horários, permitindo uma consulta rápida e organização segura da rotina de saúde.
- **Público-alvo:** Idosos, familiares e cuidadores que buscam uma ferramenta leve, sem anúncios e de fácil operação para controle de remédios.

## 🛠 Tecnologias Utilizadas

| Categoria     | Tecnologia          |
| :------------ | :------------------ |
| **Linguagem** | Python 3.10+        |
| **Interface** | CLI (Terminal)      |
| **Testes**    | Pytest              |
| **Qualidade** | Flake8 (Linting)    |
| **CI/CD**     | GitHub Actions      |

## ⚙️ Como Executar

### 1. Instalação

Certifique-se de ter o **Python** instalado em sua máquina. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/EmanuelleChristinie/Medicine.git
cd Medicine
```

### 2. Execução

Para iniciar o sistema e acessar o menu interativo:

```bash
python src/main.py
```

### 3. Testes e Lint

```bash
# Executa os testes automatizados (validação de regras de negócio e erros)
pytest

# Executa a verificação estática do código (garantia de código limpo)
flake8 src/
```

## 👩‍💻 Autora

Desenvolvido por **Emanuelle Christinie Ribeiro de Oliveira** para o Bootcamp de Ciência da Computação — Universidade CEUB.

🔗 [github.com/EmanuelleChristinie/Medicine](https://github.com/EmanuelleChristinie/Medicine)
