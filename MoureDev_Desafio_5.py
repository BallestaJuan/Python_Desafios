'''
    Reto #04 : Cadenas de caracteres
    https://retosdeprogramacion.com/roadmap/
'''
#   Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres.
#
#   Creación de cadenas 
cadena="¡Hola, Mundo!"
cadena_multilinea="""Linea 1
Linea 2
Linea 3
"""
cadena_raw=r"c:\nueva\carpeta"  # raw significa texto puro 
#
print("Cadena:", cadena)
print("Cadena multilinea:", cadena_multilinea)
print("Raw", cadena_raw)
#   Acceso a caracteres y subcadenas ( indexación y slicing)
print("\n --- Acceso y Slicing---")
print("Primer caracter:", cadena[0])
print("Último caracter:", cadena[-1])
print("Subcadena de 2 a 5:", cadena[2:5])
print("Desde la posición 7 al final:", cadena[7:])
print("cada dos caracteres:", cadena[::2])
#   Longitud de la cadena
print("\n---Longitud---")
print("Longitud de la cadena es :", len(cadena))
#   Concatenación de cadenas
print("\n---Concatenación---")
saludo="Hola"
nombre="Ana"
print(saludo+", "+nombre+"!")
#   Repetición
print("\n--- Repetición---")
print("¡"+"Python!"*3)
#   Recorrido
print("\n--- Recorrido---")
print("Caracteres uno por uno:")
for caracter in cadena:
    print(caracter, end=" ")
print()
print("Con enumerate:")
for i,c in enumerate(cadena):
    print(f"Indice {i}: '{c}")
#   Conversión de caso 
print("\n---Conversión de caso---")
texto="PyTHOn es GeNiAl"
print("Original:", texto)
print("Mayúsculas:", texto.upper())           # PYTHON ES GENIAL
print("Minúsculas:", texto.lower())           # python es genial
print("Capitalizado:", texto.capitalize())    # Python es genial
print("Título:", texto.title())               # Python Es Genial
print("Intercambiar caso:", texto.swapcase()) # pYtHoN eS gEnIaL
#   Búsqueda y verificación
print("\n--- Búsqueda y Verificación ---")
frase = "El rápido zorro marrón salta sobre el perro perezoso"
print("¿Contiene 'zorro'?:", 'zorro' in frase)                    # True
print("¿Empieza con 'El'?:", frase.startswith("El"))              # True
print("¿Termina con 'perezoso'?:", frase.endswith("perezoso"))    # True
print("Índice de 'salta':", frase.find("salta"))                  # 24
print("Índice de 'gato':", frase.find("gato"))                    # -1 (no encontrado)
print("Contar 'o':", frase.count("o"))                            # 5
#   Reemplazo
print("\n--- Reemplazo ---")
print("Reemplazar 'zorro' por 'gato':", frase.replace("zorro", "gato"))
print("Reemplazar solo 2 'o':", frase.replace("o", "O", 2))
#   División de cadenas
print("\n--- División ---")
palabras = frase.split()  # Por espacios
print("Split por espacios:", palabras)
print("Split por 'o':", frase.split("o"))
print("Split con maxsplit=2:", frase.split(" ", 2))
#   Unión de cadenas
print("\n--- Unión ---")
print("Unir con guión:", "-".join(palabras))
print("Unir con coma y espacio:", ", ".join(palabras[:3]))
# Eliminar espacios
print("\n--- Strip ---")
texto_con_espacios = "   ¡Hola!   "
print(f"Con espacios: '{texto_con_espacios}'")
print(f"Strip: '{texto_con_espacios.strip()}'")
print(f"Lstrip: '{texto_con_espacios.lstrip()}'")
print(f"Rstrip: '{texto_con_espacios.rstrip()}'")
#   Interpolación de cadenas
print("\n--- Interpolación ---")
nombre = "Carlos"
edad = 30
ciudad = "Madrid"

# f-strings (Python 3.6+)
print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}.")

# Expresiones dentro de f-strings
print(f"{nombre.upper()} tiene {edad * 12} meses.")

# Formato con alineación y relleno
print(f"Nombre: {nombre:>10}")     # Alineado a la derecha
print(f"Edad: {edad:<5} años")     # Alineado a la izquierda
print(f"Valor: {3.14159:.2f}")    # 2 decimales

# str.format() (más antiguo)
print("Hola, soy {}, tengo {} años.".format(nombre, edad))

#   Formateo de números
print("\n--- Formateo ---")
numero = 255
print(f"Binario: {numero:b}")      # 11111111
print(f"Hexadecimal: {numero:x}")  # ff
print(f"Octal: {numero:o}")        # 377
print(f"Porcentaje: {0.75:.1%}")   # 75.0%

#   Verificaciones de tipo
print("\n--- Verificaciones ---")
print("¿Es alfanumérico?:", "Python3".isalnum())      # True
print("¿Es alfabético?:", "Python".isalpha())         # True
print("¿Es numérico?:", "123".isnumeric())            # True
print("¿Es dígitos?:", "123".isdigit())               # True
print("¿Es decimal?:", "123".isdecimal())            # True
print("¿Es espacio?:", "   ".isspace())              # True
print("¿Es título?:", "Hola Mundo".istitle())         # True
print("¿Es minúsculas?:", "hola".islower())           # True
print("¿Es mayúsculas?:", "HOLA".isupper())           # True
print("¿Es imprimible?:", "abc123!".isprintable())   # True

#   Partición
print("\n--- Partición ---")
print("'abc=def=ghi'.partition('='):", "abc=def=ghi".partition("="))  # ('abc', '=', 'def=ghi')
print("'abc=def=ghi'.rpartition('='):", "abc=def=ghi".rpartition("="))  # ('abc=def', '=', 'ghi')

#   Justificación
print("\n--- Justificación ---")
texto_corto = "Python"
print(texto_corto.center(20, "-"))  # -------Python-------
print(texto_corto.ljust(20, "."))   # Python...............
print(texto_corto.rjust(20, "."))   # ...............Python

#   Expansión de tabs
print("\n--- Tabs ---")
print("Hola\tMundo".expandtabs(8))  # Hola    Mundo

#   Codificación y de codificación
print("\n--- Codificación ---")
texto = "café"
bytes_utf8 = texto.encode('utf-8')
print("Bytes UTF-8:", bytes_utf8)  # b'caf\xc3\xa9'
print("Decodificado:", bytes_utf8.decode('utf-8'))

#   Traducir
print("\n--- Traducción ---")
tabla = str.maketrans("aeiou", "12345")
print("traducción:", "hola mundo".translate(tabla))  # h4l1 m5nd4

#   Rellenar con ceros
print("\n--- ZFill ---")
print("42".zfill(5))   # 00042
print("-42".zfill(5))  # -0042

#   Casefold
print("\n--- Casefold ---")
print("ß".casefold())  # ss (útil para comparación internacional)

#   Cadenas inmutables
print("\n--- Inmutabilidad ---")
s = "hola"
# s[0] = "H"  # Error: las cadenas son inmutables
s = s.upper()  # Crea una nueva cadena
print(s)  # HOLA

#   métodos adicionales
print("\n--- Métodos útiles ---")
print("¿Es identificador válido?:", "mi_variable".isidentifier())  # True
print("¿Es ASCII?:", "café".isascii())  # False (por el acento)
print("¿Es ASCII?:", "cafe".isascii())  # True

#   Expresiones regulares
print("\n--- Expresiones regulares (módulo re) ---")
import re

texto_regex = "Mi email es usuario@dominio.com y el otro es admin@web.es"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto_regex)
print("Emails encontrados:", emails)

# Reemplazo con regex
print("Ocultar emails:", re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', texto_regex))
#
#   Resumen de métodos importantes
print("\n" + "="*50)
print("MÉTODOS DE CADENAS MÁS COMUNES:")
metodos = [
    'upper()', 'lower()', 'capitalize()', 'title()', 'swapcase()',
    'strip()', 'lstrip()', 'rstrip()',
    'split()', 'rsplit()', 'splitlines()',
    'join()', 'replace()', 'format()', 'f-strings',
    'find()', 'rfind()', 'index()', 'rindex()',
    'count()', 'startswith()', 'endswith()',
    'center()', 'ljust()', 'rjust()', 'zfill()',
    'partition()', 'rpartition()',
    'translate()', 'maketrans()', 'expandtabs()',
    'isalnum()', 'isalpha()', 'isdigit()', 'isdecimal()', 'isnumeric()',
    'islower()', 'isupper()', 'istitle()', 'isspace()', 'isprintable()',
    'isascii()', 'isidentifier()', 'casefold()',
    'encode()', 'decode()'
]
for metodo in metodos:
    print(f"  • {metodo}")

#
#   Dificultad extra:
#   Analizar dos palabras para ver si son palíndromos.
#
#  función para invertir la cadena que paso como parámetro
def inviertecadena(cadena:str) -> str:
    """
    Invierte una cadena de texto.
    
    Args:
        cadena (str): Texto a invertir.
    
    Returns:
        str: Cadena invertida.
    """
    # recorro la cadena y la pasado a otra en orden inverso
    salida=[]   # Lista para la variable de salida
    for i in range(len(cadena)-1, -1, -1):
        salida.append(cadena[i])
    return ''.join(salida)  # retorno la conversión en cadena de la lista
#
def analizapalindromos (cadena1:str, cadena2:str):
    """
    Determina si dos cadenas son palíndromos entre sí (una es inversa de la otra),
    ignorando diferencias de mayúsculas/minúsculas.
    
    Args:
        cadena1 (str): Primera cadena.
        cadena2 (str): Segunda cadena.
    
    Returns:
        imprime el resultado del análisis
    """
    if len(cadena1)==len(cadena2):
        print ("La longitud de las cadenas es idéntica. Comprobamos si es palindromo")
        #
        if inviertecadena(cadena1.lower())==cadena2.lower() or cadena1.lower()==inviertecadena(cadena2.lower()):
            print( "✓ "+cadena1+" y "+cadena2+" son palindromos \n")
        else:
            print( "✗ "+cadena1+" y "+cadena2+" NO son palindromos \n")
    else:
        print(f"✗ Las longitudes son diferentes. "
                  f"'{cadena1}' ({len(cadena1.strip())} chars) "
                  f"y '{cadena2}' ({len(cadena2.strip())} chars) "
                  f"NO pueden ser palíndromos.\n")
        return

#
# pruebas palindromos 
analizapalindromos("hola", "AlOh")
analizapalindromos("aloh", "hola")
analizapalindromos("alfa", "hola")
analizapalindromos("hola", "adios")

