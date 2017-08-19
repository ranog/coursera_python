"""
    Rodar o teste no terminal:

    python -m unittest test.py

    Não exibir 'print':

    python -m unittest -b test.py

"""
from unittest import TestCase, mock

from jogo_nim import computador_escolhe_jogada, usuario_escolhe_jogada


class TestPonto(TestCase):

    def setUp(self):
        pass

    def test_n_maior_que_m(self):
        n = 1
        m = 3
        result = computador_escolhe_jogada(n, m)
        self.assertEqual(result, n)

    def test_n_igual_m(self):
        n = 1
        m = 3
        result = computador_escolhe_jogada(n, m)
        self.assertEqual(result, n)

    def test_retornar_multiplo_de_m_mais_1(self):
        n = 5
        m = 3
        valor_esperado = 1
        result = computador_escolhe_jogada(n, m)
        self.assertEqual(result, valor_esperado)

    def test_multiplo_nao_eh_possivel_retorna_m(self):
        n = 5
        m = 4
        result = computador_escolhe_jogada(n, m)
        self.assertEqual(result, m)

    @mock.patch('builtins.input', return_value='2')
    def test_usuario_escolhe_jogada_correta(self, input_mockado):
        result = usuario_escolhe_jogada(n=10, m=3)
        self.assertEqual(result, 2)

    def test_usuario_escolheu_jogada_incorreta_depois_correta(self):
        with mock.patch('builtins.input', side_effect=[-1, 6, 5, 4, 3]):
            result = usuario_escolhe_jogada(n=5, m=3)
            self.assertEqual(result, 3)
