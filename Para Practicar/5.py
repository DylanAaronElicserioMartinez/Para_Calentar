print(" ")
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")
print(" ")
def sum(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    total = 1
    for numero in lista:
        total *= numero
    return total

# Ejemplos de uso
print(sum([1, 2, 3, 4]))  # Debería devolver 10
print(multip([1, 2, 3, 4]))  # Debería devolver 24