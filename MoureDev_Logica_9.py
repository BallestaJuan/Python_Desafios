'''
    Ejercicio #9 : Decimal a Binario
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   Crea un programa que se encargue de transformar un número decimal a binario
# sin usar funciones propias del lenguaje.
def cambiaabinario (numero:int):
    #   Manejo los casos que el número sea 0 o <0
    if numero==0:
        return('0')
    if numero <0:
        return('Error: El número no debe ser negativo')
    #   ciclo de conversión a binario
    cociente = numero
    salida =''
    # 
    while cociente >0:
        resto=cociente%2
        # añado el resto a la cadena de salida por la izd.
        salida=str(resto)+salida
        cociente=cociente//2
    return salida
#
# Pruebas
print("El binario de 2 es:"+str(cambiaabinario(2)))
print("El binario de 3 es:"+str(cambiaabinario(3)))
print("El binario de 4 es:"+str(cambiaabinario(4)))
print("El binario de 10 es:"+str(cambiaabinario(10)))
print("El binario de 19 es:"+str(cambiaabinario(19)))