#
# Desafío #00 : https://retosdeprogramacion.com/roadmap/
#
# El lenguaje de programación elegído es :  https://www.python.org/
#
# Sintaxis de comentarios 

# Este es un tipo de comentario 
x = 3.14 # Este es otro tipo de comentario
"""
 Este es otro tipo de comentario
 en varias lineas. 
 que se abre y cierra por triples comillas
 """
x = 2 
'''
 Existe la posibilidad también de hacer las comillas
 de apertura y cierre de tipo simple
'''
x = x + 3
#
# Creación de variables de tipo de datos primitivos 
variable_1 = 3
variable_2 = 3.14
variable_3 = "Python"
variable_4= True
#
print("Tipo de la primera variable "+str(type(variable_1))+"\n")
print("Tipo de la segunda variable "+str(type(variable_2))+"\n")
print("Tipo de la tercera variable "+str(type(variable_3))+"\n")
print("Tipo de la cuarta variable "+str(type(variable_4))+"\n")

# Python permite tipos de datos adicionales 
variable_5 = ["Juan", "Pedro", "Luis"]  # list
variable_6  = (45, 90)  # tuple
variable_7 = {"rojo", "verde", "azul"}  # set
variable_8 = {"nombre": "Ana", "edad": 30}  # dict
variable_9 = None       # None
# usando f strings para evitar la función str()
print(f"Tipo de la quinta variable {type(variable_5)}\n")
print(f"Tipo de la sexta variable {type(variable_6)}\n")
print(f"Tipo de la septima variable {type(variable_7)}\n")
print(f"Tipo de la octava variable {type(variable_8)}\n")
print(f"Tipo de la novena variable {type(variable_9)}\n")
#
print ("¡Hola, Python!")