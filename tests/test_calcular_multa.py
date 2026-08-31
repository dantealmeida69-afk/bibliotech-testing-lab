from src.bibliotech import calcular_multa


def test_sem_atraso():
    assert calcular_multa(0) == 0.0


def test_atraso_negativo():
    assert calcular_multa(-2) == 0.0


def test_atraso_dentro_da_faixa_leve():
    assert calcular_multa(3) == 6.0


def test_atraso_no_limite_da_faixa_leve():
    assert calcular_multa(7) == 14.0


def test_atraso_logo_apos_o_limite():
    assert calcular_multa(8) == 17.0


def test_atraso_maior_na_faixa_grave():
    assert calcular_multa(10) == 23.0
