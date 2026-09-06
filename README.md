
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



