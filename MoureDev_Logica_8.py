'''
    Ejercicio 8: Contando palabras
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   Crea un programa que cuenta cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#- los signos de puntuación no forman parte de la palabra
#- una palabra es la misma aparezca en mayúsculas y minúsculas
#- no se pueden utilizar funciones propias del lenguaje
import re   # para uso de expresiones regulares
#
def cuentapalabras (cadena:str):
    resultado={} # para almacenar la salida en forma de diccionario, la palabra es la clave y el valor el número de veces que aparecer
    #
    cadenanormalizada=cadena.lower()                                # lo cambio a minúsculas, para simplificar la comparativa
    cadenasinpuntuacion=re.sub(r'[^\w\s]','', cadenanormalizada)    # quito los caracteres que no son texto o espacio
    # trozeo en una lista y ordeno para que las palabras repetidas caigan juntas
    lista=cadenasinpuntuacion.split()
    # bucle para contar palabras, si ya esté en el diccionario +1 y si no está =1
    for palabra in lista:
        if palabra in resultado:
            resultado [palabra] +=1
        else:
            resultado[palabra]=1
    return(resultado)
#
#   Pruebas           
print(cuentapalabras("Hoy hace un día muy soleado."))
print(cuentapalabras("Un día, dos días, tres días. Como me gustan los días."))
print(cuentapalabras("Juan juega todo los días a jugar, juega en casa, juega en el campo."))