print(" ")
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")
print(" ")
def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    palabra = palabra.lower()
    # Comparamos la palabra con su reverso
    return palabra == palabra[::-1]

# Ejemplo de uso
print(es_palindromo("radar"))  # Debería devolver True
print(es_palindromo("hola"))   # Debería devolver False