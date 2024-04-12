from vocales import contar_vocales
import unittest


class TestContarVocales (unittest.TestCase):
    
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_contar_cas (self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_casa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_este(self):
        resultado = contar_vocales('este')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_auto(self):
        resultado = contar_vocales('auto')
        self.assertEqual(resultado, {'a': 1 , 'u': 1 , 'o': 1})

    def test_contar_PALABRA(self):
        reesultado = contar_vocales('palabra')
        self.assertEqual(reesultado, {'a': 3})

    def test_contar_esdrújulas(self):
        resultado = contar_vocales('esdrújulas')
        self.assertEqual(resultado, {'e': 1 , 'ú': 1 , 'u': 1, 'a': 1})

    def test_contar_TERMINAL(self):
        resultado = contar_vocales('terminal')
        self.assertEqual(resultado, {'e': 1 , 'i': 1 , 'a': 1})

    def test_contar_abrió(self):
        resultado = contar_vocales('abrió')
        self.assertEqual(resultado, {'a': 1 , 'i': 1 , 'ó': 1})
    
    def test_contar_SANTIAGO(self):
        resultado = contar_vocales('santiago')
        self.assertEqual(resultado, {'i': 1 , 'o': 1 , 'a': 2})

    def test_contar_canción(self):
        resultado = contar_vocales('canción')
        self.assertEqual(resultado, {'a': 1 , 'i': 1 , 'ó': 1})

    def test_contar_argumnetación(self):
        resultado = contar_vocales('argumentación')
        self.assertEqual(resultado, {'u': 1 , 'e': 1 , 'i': 1 , 'ó': 1 , 'a': 2})

    def test_contar_matemáticas(self):
        resultado = contar_vocales('matemáticas')
        self.assertEqual(resultado, {'e': 1 , 'i': 1 , 'á': 1 , 'a': 2 })
    
    def test_contar_colibrí(self):
        resultado = contar_vocales('colibrí')
        self.assertEqual(resultado, {'o': 1 , 'i': 1 , 'í': 1})

    def test_contar_hincapié(self):
        resultado = contar_vocales('hincapié')
        self.assertEqual(resultado, {'a': 1 , 'é': 1 , 'i': 2})

unittest.main()