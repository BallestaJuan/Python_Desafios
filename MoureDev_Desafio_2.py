'''
    Desafio #01 Operadores y estructuras de control
    https://retosdeprogramacion.com/roadmap/
'''
#   Operadores Aritmeticos
a = 11
b = 5 
print("Operadores Aritméticos:")
print("Suma : ", a+b)
print("Resta : ", a-b)
print("Multiplicación : ", a*b)
print("División : ", a/b)
print("División entera:", a//b)
print("Módulo:", a%b)
print("Potencia : ", a**b)
#   Operadores lógicos
x=True
y=False
print("Operadores Lógicos")
print("And:", x and y )
print("Or:", x or y )
print("Not x:", not x)
#   Operadores de asignacion
c = 5
print("Operadores de Asignación:")
print("Valor inicial:", c)
c += 2
print("c += 2:", c)
c -= 1
print("c -= 1:", c)
c *= 3
print("c *= 3:", c)
c /= 2
print("c /= 2:", c)
c %= 4
print("c %= 4:", c)
c **= 2
print("c **= 2:", c)
c //= 2
print("c //= 2:", c)
#   Operadores de bit
m = 5      # binario: 101
n = 3      # binario: 011

print("Operadores de Bit:")
print("AND (m & n):", m & n)   # 001 -> 1
print("OR (m | n):", m | n)    # 111 -> 7
print("XOR (m ^ n):", m ^ n)   # 110 -> 6
print("NOT (~m):", ~m)         # complemento de 5 -> -6
print("Desplazamiento a izquierda (m << 1):", m << 1)  # 1010 -> 10
print("Desplazamiento a derecha (m >> 1):", m >> 1) # 010 -> 2
print("-" * 30)
#   Estructuras condicionales
print("Estructura condicional :")
num=7
if num>10:
    print ("mayor que 10")
elif num==10:
    print("igual a 10")
else:
    print("menor que 10")
#   estructuras itereativas 
print("Estructuras Iterativas:")

# Bucle For 
print("Bucle tipo For:")
for i in range(3):
    print("i =", i)

# Bucle While
print("Bucle tipo While:")
j = 0
while j < 3:
    print("j =", j)
    j += 1
#   Manejo de exceptciones
print("Manejo de Excepciones:")

try:
    num1 = int(input("Introduce un número: "))
    resultado = 10 / num1
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes introducir un número entero.")
finally:
    print("Fin del bloque try-except.")

#   Crear un programa que imprima por consola los números entre 10 10 y 55 incl. pero no el 16 ni multiplos de 3
for i in range(10,56) :
    if i!=16 and i%3!=0:
        print (i)