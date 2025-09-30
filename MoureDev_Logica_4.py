'''
    Ejercicio #4 : ¿ es un número primo?
    https://retosdeprogramacion.com/ejercicios
'''
#
#   Defino una función para comprobar si el número es primo
# compruebo el módulo con 2,3,5 si es cero, el número no es primo
def NumPrimo (numero):
    #
    if numero <=1:
        return False
    if numero<=3:
        return True
    if numero%2==0 or numero%3==0:
        return False
    #   compruebo multipls de 2 y 3 en adelante
    i=5
    # comprobamos a partir de 2 y 3 hasta la raiz de número
    # porque raiz*raiz = numero. Los números primos después de 3 tienen la forma 6k+/-1
    while i*i <=numero:
        if numero%i==0 or numero%(i+2)==0:
            return False
        i+=6        
    return True

#
#
print(f"El número 2 ¿es primo? {NumPrimo(2)}")
print(f"El número 9 ¿es primo? {NumPrimo(9)}")
print(f"El número 13 ¿es primo? {NumPrimo(13)}")
print(f"El número 29 ¿es primo? {NumPrimo(29)}")
print(f"El número 121 ¿es primo? {NumPrimo(121)}")
