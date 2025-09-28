'''
    Ejercicio #3 : La sucesión de Fibonnacci
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   prepararo una variable tipo lista donde voy a añadir los miembros de la sucesión y me deja direccionar elemento a elemento de forma sencilla
Sucesion=[1, 1 ]
#
#   hago un bucle de 50 posiciones (las dos primeras ya están cargadas en la lista) para crear la sucesión de Fibonacci
for i in range(2, 48):
    Sucesion.append (Sucesion[i-2]+Sucesion[i-1])
#
#   Imprimo por pantalla la solución
print(Sucesion)