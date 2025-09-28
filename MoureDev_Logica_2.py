'''
    Ejercicio #2 ¿Es un anagrama?
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   Defino una función Anagrama que compara las dos cadenas
# - si las dos cadenas son iguales 
# - si la cadena1 ordenada es igual a cadena2 ordenada ( quiere decir que tienen en mismo número de caracteres y mismos caracteres)
def anagrama (cadena1:str, cadena2:str):
    if cadena1==cadena2 :
        salida="Son cadenas idénticas"
    else:
        if sorted(cadena1)==sorted(cadena2):
            salida="Es Anagrama"
        else:
            salida="NO es anagrama"
    #
    return salida
#
#   Hago algunas pruebas para comprobar el funcioanmiento
print(anagrama("hola", "hloa"))   # Es anagrama
print(anagrama("hola", "halo"))   # Es anagrama
print(anagrama("hola", "hella"))  # No es anagrama
print(anagrama("hola", "hola"))   # Son cadenas idénticas

