from unittest import TestCase, main
from expr.matematica import avaliador


class TestExprMatematica(TestCase):
    def test_2_mais_5(self):
        esperado = 7
        expressao = '2 5 +'
        self.assertEqual(esperado, avaliador(expressao))

    def test_3_vezes_7(self):
        esperado = 21
        expressao = '3 7 *'
        self.assertEqual(esperado, avaliador(expressao))

    def test_21_dividido_por_7(self):
        esperado = 3
        expressao = '21 7 /'
        self.assertEqual(esperado, avaliador(expressao))

    def test_3_menos_7(self):
        esperado = -4
        expressao = '3 7 -'
        self.assertEqual(esperado, avaliador(expressao))

    def test_3_vezes_2_mais_5(self):
        esperado = 21
        expressao = '3 2 5 + *'
        self.assertEqual(esperado, avaliador(expressao))

    def test_7_vezes_5_mais_3_dividido_6_menos_10(self):
        esperado = 29.75
        expressao = '7 5 3 6 10 - / + *'
        self.assertEqual(esperado, avaliador(expressao))

    def test_10_dividido_por_0(self):
        expressao = '10 0 /'
        with self.assertRaises(ZeroDivisionError):
            avaliador(expressao)

    def test_2_elevado_3(self):
        expressao = '2 3 ^'
        esperado = 8
        self.assertEqual(esperado, avaliador(expressao))

    def test_5_fatorial(self):
        expressao = '5 !'
        esperado = 120
        self.assertEqual(esperado, avaliador(expressao))

    def test_5_termial(self):
        expressao = '5 ?'
        esperado = 15
        self.assertEqual(esperado, avaliador(expressao))


if __name__ == '__main__':
    main()
