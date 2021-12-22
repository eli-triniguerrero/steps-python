#TUPLAS
my_tuple = (1, 'hola', True)
print(my_tuple[0])

# >>> my_tuple = (1, 'hola', True)
# >>> type(my_tuple)
# <class 'tuple'>

# >>> tuple_two = (1)
# >>> type(tuple_two)
# <class 'int'>

# >>> tuple_two = (1,)
# >>> type(tuple_two)
# <class 'tuple'>

# >>> my_other_tuple = (2, 3, 4)

# >>> my_tuple += my_other_tuple #reasignacion
# >>> print(my_tuple)
# (1, 'hola', True, 2, 3, 4)

# >>> def coordenadas():
# ...     return(5, 4)
# ... 
# >>> coordenada = coordenadas()
# >>> coordenada
# (5, 4)
# >>> x, y = coordenadas()
# >>> print(x, y)
# 5 4
# >>> x
# 5
# >>> y
# 4
# >>> #desempaquetar

#RANGOS
#  >>> # range(comienzo, fin, pasos)
# >>> my_range = range(1, 5)
# >>> type(my_range)
# <class 'range'>
# >>> for i in my_range:
# ...     print(i)
# ... 
# 1
# 2
# 3
# 4
# >>> my_range = range(0, 7 ,2)
# >>> my_other_range = range(0, 8, 2)
# >>> my_range == my_other_range
# True
# >>> for i in my_range:
# ...     print(i)
# ... 
# 0
# 2
# 4
# 6
# >>> for i in my_other_range:
# ...     print(i)
# ... 
# 0
# 2
# 4
# 6
# >>> id(my_range)
# 140674128060208
# >>> my_range is my_other_range
# False
# >>>

#genrar un rango con los numeros nones
# >>> for i in range(1, 100, 2):
# ...     print(i)
# ... 
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# ...
# 99

