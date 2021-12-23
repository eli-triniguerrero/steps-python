#CAJA DE CRISTAL
# Las pruebas de caja cristal asumen que ya existe codigo escrito 

import unittest

# def verificar_edad(edad):
#     if edad >= 18:
#         return True
#     else:
#         return False

# class PruebaCristalTest(unittest.TestCase):
#     #verificar si es mayor
#     def test_mayor_de_edad(self):
#         edad = 20

#         resultado = verificar_edad(edad)
#         self.assertEqual(resultado, True)

#     #verificar que es menor
#     def test_menor_de_edad(self):
#         edad = 10

#         resultado = verificar_edad(edad)
#         self.assertEqual(resultado, False)
        
'''
..
----------------------------------------------------------------------
Ran 2 test in 0.000s

OK
'''

#intento 2
def verificar_edad(edad):
    if edad >= 18:
        return False
    else:
        return False

class PruebaCristalTest(unittest.TestCase):
    #verificar si es mayor
    def test_mayor_de_edad(self):
        edad = 20

        resultado = verificar_edad(edad)
        self.assertEqual(resultado, True)

    #verificar que es menor
    def test_menor_de_edad(self):
        edad = 10

        resultado = verificar_edad(edad)
        self.assertEqual(resultado, False)

'''
F.
======================================================================
FAIL: test_mayor_de_edad (__main__.PruebaCristalTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/trinityhome/Desktop/steps-python/stepspy/20_cajacristal.py", line 48, in test_mayor_de_edad
    self.assertEqual(resultado, True)
AssertionError: False != True

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
'''


if __name__ == '__main__':
    unittest.main()