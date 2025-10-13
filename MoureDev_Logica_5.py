'''
    Ejercicio 5: área de un polígono
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   Diseña una función (importante que sólo sea una) que se capaz de calcular y retornar el área de un polígono.
# defino los tipos de polígonos en variables mediante una clase, con los componentes que van a tener.
# se que la forma correcta de hacerlo, seria añadir a cada clase su propio cálculo de área. En este caso el ejercicio pide una función.
class Cuadrado:
    def __init__(self, lado:float):
        self.lado = lado
class Triangulo:
    def __init__ (self, base:float, altura:float):
        self.base=base
        self.altura=altura
class Rectangulo:
    def __init__(self, base:float, altura:float):
        self.base=base
        self.altura=altura
# defino los poligonos que quiero calcular 
cuad=Cuadrado(5.2)
tria=Triangulo(4.3, 2.3)
rect=Rectangulo(3,4)
# defino la función que comprueba que tipo es de variable ( con la función isinstance) y elige el cálculo
def calcula_area (poligono):
    if isinstance(poligono, Cuadrado):
        print (f"Se trata de un cuadrado. Su área es: {poligono.lado**2}")
    elif isinstance(poligono, Triangulo):
        print (f"Se trata de un triángulo. Su área es: {0.5*(poligono.base*poligono.altura)}")
    elif isinstance(poligono, Rectangulo):
        print (f"Se trata de un rectangulo. Su área es: {(poligono.base*poligono.altura)}")
    else:
        print(f"Tipo de polígono no reconocido: {type(poligono).__name__}")
# llamo a la función con cada una de los polígonos que he creado
calcula_area(cuad)
calcula_area(tria)
calcula_area(rect)