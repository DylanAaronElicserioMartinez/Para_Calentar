print(" ")
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")
print(" ")
caracter=input("Ingresa una palabra:")
def es_vocal(caracter):
    # Convertimos el carácter a minúscula para manejar tanto mayúsculas como minúsculas
    caracter = caracter.lower()
    # Verificamos si el carácter es una vocal
    return caracter in "aeiou" 