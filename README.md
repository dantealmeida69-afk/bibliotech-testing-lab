# bibliotech-testing-lab

Repositório de apoio para a aula prática **"Missão QA: testando o BiblioTech"**.

## Cenário

O time de desenvolvimento do BiblioTech (uma biblioteca digital) entregou uma nova
versão do módulo de empréstimos. Antes do deploy, o time de QA (vocês!) precisa
verificar se as regras de negócio estão corretas, usando testes de **caixa preta**
e **caixa branca**.

## Estrutura do repositório

```
bibliotech-testing-lab/
│
├── README.md
├── requisitos.md              # Requisitos funcionais (RF01, RF02, RF03)
├── requirements-dev.txt       # Dependências de teste
│
├── src/
│   ├── __init__.py
│   └── bibliotech.py          # Código a ser testado
│
├── tests/
│   └── __init__.py            # Seus testes pytest vão aqui
│
├── docs/
│   ├── plano_testes.md        # Mini Plano de Testes (preencher)
│   ├── roteiro_testes.md      # Modelo de caso de teste (preencher)
│   └── matriz_rastreabilidade.md
│
└── .github/
    └── workflows/
        └── tests.yml          # CI: roda pytest + cobertura em cada push/PR
```

## Como começar

```bash
git clone <URL_DO_REPOSITORIO>
cd bibliotech-testing-lab
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

Crie sua branch de equipe:

```bash
git checkout -b testes/equipe-XX
```

## Rodando os testes

```bash
pytest -v
```

## Rodando com cobertura

```bash
pytest --cov=src --cov-branch --cov-report=term-missing
```

Meta da equipe: **≥ 90% de cobertura de linhas e branches**, sem testes criados
apenas para "inflar" o número.

## Fluxo esperado

1. Leiam `requisitos.md` (ainda **sem** abrir `src/bibliotech.py`).
2. Preencham o Mini Plano de Testes (`docs/plano_testes.md`).
3. Escrevam casos de teste de **caixa preta** (mínimo 4 por função) e documentem
   pelo menos um em `docs/roteiro_testes.md`.
4. Implementem os testes em `tests/` e rodem `pytest -v`.
5. Só então abram `src/bibliotech.py` e façam a análise de **caixa branca**
   (decisões, condições, caminhos).
6. Rodem a cobertura e completem os testes que faltam.
7. Preencham `docs/matriz_rastreabilidade.md`.
8. Commitem, deem push e abram um Pull Request usando o template.
9. Aguardem o GitHub Actions rodar e revisem o PR de outra equipe.

Boa missão! 🕵️‍♀️📚
