'''
    Reto #02: Funciones y alcance
    https://retosdeprogramacion.com/roadmap/
'''
#
#
def ejemplo_sin_parametros_ni_retorno():
    print("Esta función no tiene parámetros ni retorna nada.")

def ejemplo_con_parametros_sin_retorno(nombre: str, edad: int):
    print(f"Hola, {nombre}. Tienes {edad} años.")

def ejemplo_sin_parametros_con_retorno() -> str:
    return "Esta función no tiene parámetros pero retorna un string."

def ejemplo_con_parametros_con_retorno(a: int, b: int) -> int:
    return a + b
#   Función dentro de función
def funcion_externa():
    def funcion_interna():
        print("Esta es una función interna.")
    funcion_interna()
    print("Esta es la función externa.")
#   Funciones disponibles en el lenguaje 
longitud = len("Python")
print(f"Longitud de 'Python': {longitud}")
#   Variables locales y globales
variable_global = "Soy global"
#
def prueba_variables():
    variable_local = "Soy local"
    print("Dentro de la función:")
    print(variable_local)  # Accesible
    print(variable_global)  # Accesible
#
prueba_variables()
print("Fuera de la función:")
try:
    print(variable_local)  # No accesible, error
except NameError:
    print("variable_local no está definida (local).")
print(variable_global)  # Accesible

def modificar_global():
    global variable_global
    variable_global = "Global modificada"

modificar_global()
print("Global después de modificación:", variable_global)
#

''' 
    Crea una función que reciba dos parametros tipo cadena de texto 
    y retorne un número 
'''
#
#
def comprueba_datos (param_1:str, param_2:str) -> int:
    cuenta=0
    #
    for i in range(1, 101):
        if i%3==0 and i%5==0 :
            print(param_1 +" "+ param_2)
        elif i%3==0:
            print(param_1)
        elif i%5==0:
            print(param_2)
        else:
            cuenta +=1
            print(i) 
    #
    return cuenta
#
print("Número de veces que se ha impreso un número :", comprueba_datos("hola", "adios"))