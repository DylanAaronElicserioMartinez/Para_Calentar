print(" ")
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")
print(" ")
def calcular_longitud(elemento):
    contador = 0
    for _ in elemento:  # Iteramos sobre cada elemento en la lista o cadena
        contador += 1   # Aumentamos el contador en 1 por cada elemento
    return contador

# Ejemplos de uso
lista = [1, 2, 3, 4, 5]
cadena = "Hola, mundo!"

print(calcular_longitud(lista))  # Salida: 5
print(calcular_longitud(cadena))  # Salida: 13