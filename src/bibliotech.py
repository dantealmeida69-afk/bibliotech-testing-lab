"""
Módulo de empréstimos do BiblioTech.

Este código foi entregue pela equipe de desenvolvimento e está prestes a ir
para produção. Cabe à equipe de QA validar se ele atende aos requisitos
descritos em `requisitos.md`.
"""

LIMITE_EMPRESTIMOS = 3


def pode_emprestar(usuario_ativo, possui_pendencia, emprestimos_ativos):
    """
    RF01 — Um usuário pode realizar um novo empréstimo quando:
    - está ativo;
    - não possui pendências;
    - possui menos de 3 empréstimos ativos.
    """
    if not usuario_ativo:
        return False
    if possui_pendencia:
        return False
    # Existe um defeito proposital nesta condição.
    if emprestimos_ativos > LIMITE_EMPRESTIMOS:
        return False
    return True


def calcular_multa(dias_atraso):
    """
    RF02 — Cálculo da multa por atraso.
    """
    if dias_atraso <= 0:
        return 0.0
    if dias_atraso <= 7:
        return dias_atraso * 2.0
    dias_excedentes = dias_atraso - 7
    return 14.0 + (dias_excedentes * 3.0)


def classificar_atraso(dias_atraso):
    """
    RF03 — Classificação textual do atraso.
    """
    if dias_atraso <= 0:
        return "sem atraso"
    elif dias_atraso <= 7:
        return "atraso leve"
    elif dias_atraso <= 30:
        return "atraso moderado"
    else:
        return "atraso grave"
