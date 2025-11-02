'''
    Ejercicio #10: Código morse
    https://retosdeprogramacion.com/ejercicios/
'''
#
#   Crea  un programa que sea capaz de transformar texto natural a morse y viceversa
#
import string
#   Ya que se trata de un programa bidireccional (texto <-->Morse) voy  a trabajar con un diccionario
# en dirección de texto a morse y una lista de morse a texto.
class listabidireccional:
    def __init__(self):
        self.clave_a_valor={}   # el diccionario de texto a morse
        self.valor_a_clave=[]   # la lista de morse a texto
    # para cargar el diccionario von valores
    def add(self, clave, valor):
        self.clave_a_valor[clave]=valor
        self.valor_a_clave.append((valor, clave))
    def obten_valor (self, clave):
        return self.clave_a_valor.get(clave)
    def obten_clave(self, valor):
        return [k for v, k in self.valor_a_clave if v == valor]
#   preparo la variable para contener los datos como tipo lista bidireccional 
bd = listabidireccional()
#   Cargo el alfabeto morse de la URL (esta forma de hacerlo me evita depender de la carga de un fichero externo con la información)
MORSE_ALFABETO = {
    "a": "._", "b": "_...", "c": "_._.", "ch": "____", "d": "_..", "e": ".",
    "f": ".._.", "g": "__.", "h": "....", "i": "..", "j": ".___", "k": "_._",
    "l": "._..", "m": "__", "n": "_.", "ñ": "__.__", "o": "___", "p": ".__.",
    "q": "__._", "r": "._.", "s": "...", "t": "_", "u": ".._", "v": "..._",
    "w": ".__", "x": "_.._", "y": "_.__", "z": "__..", "0": "_____", "1": ".____",
    "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....",
    "7": "__...", "8": "___..", "9": "____.", ".": "._._._", ",": "__..__", "?": "..__.."
}
#
for clave, valor in MORSE_ALFABETO.items():
    bd.add(clave, valor)
# pruebo que la lista funciona en ambas direcciones 
# print(bd.obten_valor("a"))  # Imprime: a
# print(bd.obten_clave("_ _.."))     # Imprime: ['z']
#   guardo lo que hay que convertir en una dirección o en la otra en la  variable cadena        
#cadena="Hola, como estas?"
cadena=".... ___ ._.. ._ __..__ _._. ___ __ ___ . ... _ ._ ... ..__.."
#
# Comprobar si la cadena solo contiene letras, números, puntuación y espacios
if all(c in ". _" for c in cadena):
    print("La cadena solo contiene '.', '_' y espacios.")
    lista=cadena
    lista=lista.split(" ")      # separo por los espacios la lista en caracteres mores
    #   
    i=0
    while i < len(lista):
        print(bd.obten_clave(lista[i]))
        i+=1
elif all(c.isalnum() or c in string.punctuation or c==" " for c in cadena):
    print("La cadena solo contiene letras, números y puntuación. Hay que convertir a Morse")
    cadena=cadena.lower()     # normalizo la cadena internamente a minúsculas, los caracteres los he declarado como minúsculas
    lista=list(cadena)        # separo la cadena caracter por caracter
    # recorro la lista y convierto a morse
    for i in range(len(lista)):
        print(bd.obten_valor(lista[i]))
# Comprobar si la cadena solo contiene ".", "_" y " "
else:
    print("La cadena contiene otros caracteres, que no es posible convertir.")

