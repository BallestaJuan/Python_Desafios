'''
    Reto #03 : Estructuras de datos 
    https://retosdeprogramacion.com/roadmap/
'''
#
#   Muestra ejemplos de creacion de todas las estructuras soportadas por defecto
# Utiliza operaciones de inserción, borrado, actualización y ordenación.
# 
#   Estructura de datos : List
# Crear una lista
mi_lista=[1,2,3]
# Inserción
mi_lista.append (4)     # añadir al final
mi_lista.insert(1,5)    # insertar en el indice 1
mi_lista.extend([6,7])  # añadir otra lista
#
print(mi_lista)
# Borrado
mi_lista.remove(5)      # borra la primera ocurrencia
ultimo =mi_lista.pop()  # Borra y retorna el ultimo 
del mi_lista[0]         # borra el indice 0
# Actualización 
mi_lista[0]=10
# Ordenación
mi_lista.sort()
ordenada=sorted(mi_lista, reverse=True)
print(mi_lista)
#
#   Estructura de datos : tuple
# Crear tupla
mi_tupla = (1, 2, 3)
# Inserción (crea nueva)
nueva_tupla = mi_tupla + (4,)  # [1, 2, 3, 4]
# Borrado (crea nueva, ej. sin índice 1)
nueva_tupla = mi_tupla[:1] + mi_tupla[2:]  # (1, 3)
# Actualización (crea nueva, ej. cambia índice 0)
nueva_tupla = (10,) + mi_tupla[1:]  # (10, 2, 3)
# Ordenación
ordenada = sorted(mi_tupla)  # Nueva lista: [1, 2, 3]
print(ordenada)
#
#   Estrctura de datos: Dict
# Crear dict
mi_dict = {'a': 1, 'b': 2}
# Inserción
mi_dict['c'] = 3  # {'a': 1, 'b': 2, 'c': 3}
# Borrado
del mi_dict['a']  # {'b': 2, 'c': 3}
valor = mi_dict.pop('b')  # Borra y retorna: {'c': 3}, valor=2
# Actualización
mi_dict['c'] = 10  # {'c': 10}
# Ordenación (por claves)
ordenado_claves = sorted(mi_dict)  # ['c']
ordenado_items = sorted(mi_dict.items())  # [('c', 10)]
print(ordenado_items)
#
#   Estructura de datos : Set
# Crear set
mi_set = {1, 2, 3}
# Inserción
mi_set.add(4)  # {1, 2, 3, 4} (no duplica si ya existe)
# Borrado
mi_set.remove(2)  # Borra 2: {1, 3, 4} (error si no existe)
mi_set.discard(5)  # No error si no existe: {1, 3, 4}
elemento = mi_set.pop()  # Borra y retorna aleatorio: {1, 3}, elemento=4 (ej.)
# Actualización (no directo; combina operaciones)
mi_set.discard(1)  # Borra
mi_set.add(10)  # Agrega: {3, 10}
# Ordenación
ordenado = sorted(mi_set)  # Nueva lista: [3, 10]
print(ordenado)
#
#   Estrucutra de datos : Conjunto inmutable / Frozenset
# Crear frozenset
mi_frozenset = frozenset([1, 2, 3])
# Inserción (crea nueva)
nuevo_frozenset = frozenset(mi_frozenset | {4})  # frozenset({1, 2, 3, 4})
# Borrado (crea nueva)
nuevo_frozenset = frozenset(s for s in mi_frozenset if s != 2)  # frozenset({1, 3})
# Actualización (crea nueva)
nuevo_frozenset = frozenset((10,) + tuple(mi_frozenset)[1:])  # frozenset({10, 3}) (ej. cambia 1 por 10)
# Ordenación
ordenado = sorted(mi_frozenset)  # Nueva lista: [1, 2, 3]
print(ordenado)
#
#
