from src.bibliotech import classificar_atraso


def test_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"


def test_atraso_leve_no_limite_inferior():
    assert classificar_atraso(1) == "atraso leve"


def test_atraso_leve_no_limite_superior():
    assert classificar_atraso(7) == "atraso leve"


def test_atraso_moderado_no_limite_inferior():
    assert classificar_atraso(8) == "atraso moderado"


def test_atraso_moderado_no_limite_superior():
    assert classificar_atraso(30) == "atraso moderado"


def test_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"
