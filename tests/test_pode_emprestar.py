from src.bibliotech import pode_emprestar


def test_usuario_ativo_sem_pendencia_dentro_do_limite():
    assert pode_emprestar(True, False, 0) is True


def test_usuario_inativo_nao_pode_emprestar():
    assert pode_emprestar(False, False, 0) is False


def test_usuario_com_pendencia_nao_pode_emprestar():
    assert pode_emprestar(True, True, 0) is False


def test_usuario_no_limite_de_3_emprestimos_nao_pode_emprestar():
    # Caso de fronteira: o requisito diz "menos de 3 empréstimos ativos",
    # ou seja, com 3 empréstimos o empréstimo já deveria ser recusado.
    assert pode_emprestar(True, False, 3) is False


def test_usuario_com_2_emprestimos_pode_emprestar():
    assert pode_emprestar(True, False, 2) is True
