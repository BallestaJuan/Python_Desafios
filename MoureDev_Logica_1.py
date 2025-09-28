'''
    Ejercicio #1 : El Famoso "Fizz Buzz"
    https://retosdeprogramacion.com/ejercicios/
'''

for i in range(1,101):
    # si es múltiplo de 3 y de 5 imprimo "fizzbuzz"
    if (i%3==0) and (i%5==0):
        print("fizzbuzz")
    # si es múltiplo de 3 imprimo "fizz"
    elif (i%3==0):
        print("fizz")
    # si es múltiplo de 4 imprimo "buzz"
    elif (i%5==0):
        print ("buzz")
    # si no cummple ninguna de las condiciones anteriores imprimo el númmero
    else:
        print(i)


