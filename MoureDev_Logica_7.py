'''
    Ejercicio 7: Invirtiendo cadenas
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   Crea  un programa que invierta una cadena de texto, sin usar funciones propias del lenguaje
def inviertecadena (cadena:str) -> str:
    cadenatrabajo=list(cadena)
    cadenasalida=[]
    #
    for i in range(len(cadena)-1, -1, -1):
        cadenasalida.append(cadenatrabajo[i])
    # convertimos la lista 
    return ''.join(cadenasalida)
# pruebas
print ("Invierte hola: "+inviertecadena("hola"))
print ("Invierte Hola Mundo: "+inviertecadena("Hola Mundo"))
print ("Invierte Gaazpacho: " +inviertecadena("Gazpacho"))

