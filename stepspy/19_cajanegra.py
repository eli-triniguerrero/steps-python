# PRUEBAS DE CAJA NEGRA

#Prueba 'inputs y valida 'outputs'
# Unit testing: 
## Probar función por función 

# Integration testing:
## Cuando todos los módulos funcinan entre si


import unittest

# class CajaNegraTest(unittest.TestCase):
#     #pruebas que se hacen para revisar una funcion
#     #planteacion varios casos posibles
#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1 + num_2)

#         self.assertEqual(resultado, 15)

''' 
# ||||||||RESULTADO EN CONSOLA |||||||||||||||||
E
======================================================================
ERROR: test_suma_dos_positivos (__main__.CajaNegraTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/trinityhome/Desktop/steps-python/stepspy/19_cajanegra.py", line 11, in test_suma_dos_positivos
    resultado = suma(num_1 + num_2)
NameError: name 'suma' is not defined
----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
'''
#intento 2
# def suma():
#     pass

# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1 + num_2)

#         self.assertEqual(resultado, 15)
'''
----------RESULTADO EN CONSOLA---------------------
E
======================================================================
ERROR: test_suma_dos_positivos (__main__.CajaNegraTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/trinityhome/Desktop/steps-python/stepspy/19_cajanegra.py", line 41, in test_suma_dos_positivos
    resultado = suma(num_1 + num_2)
TypeError: suma() takes 0 positional arguments but 1 was given

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
'''

# INTENTO 3
# def suma(num_1, num_2):
#     pass    

# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1 + num_2)

#         self.assertEqual(resultado, 15)
'''
E
======================================================================
ERROR: test_suma_dos_positivos (__main__.CajaNegraTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/trinityhome/Desktop/steps-python/stepspy/19_cajanegra.py", line 70, in test_suma_dos_positivos
    resultado = suma(num_1 + num_2)
TypeError: suma() missing 1 required positional argument: 'num_2'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
'''

#intento 4
# def suma(num_1, num_2):
#     return num_1 + num_2    

# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)
'''
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

#intento 5
# def suma(num_1, num_2):
#     return num_1 + num_2    

# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)
    
#     def test_suma_dos_negativos(self):
#         num_1 = -10
#         num_2 = -7

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, -17)
'''
.. <-- dos test OK
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''

#intento 6 
def suma(num_1, num_2):
    return abs(num_1) + num_2    

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)
    
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

'''
F.
======================================================================
FAIL: test_suma_dos_negativos (__main__.CajaNegraTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/trinityhome/Desktop/steps-python/stepspy/19_cajanegra.py", line 159, in test_suma_dos_negativos
    self.assertEqual(resultado, -17)
AssertionError: 3 != -17

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
'''


        



if __name__ == '__main__':
    unittest.main()

