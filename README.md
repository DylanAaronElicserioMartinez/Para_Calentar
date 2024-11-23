# Para_Calentar
Actividad en clase

#Codigo 1

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def max(num1, num2):

    if num1 > num2:
    
        return num1
        
    else:
    
        return num2

# Ejemplo de uso

resultado = max(10, 20)

print("El mayor es:", resultado)  # Debería imprimir: El mayor es: 20

![image](https://github.com/user-attachments/assets/85b486dc-61e9-443f-a9aa-938bc223757e)

![image](https://github.com/user-attachments/assets/e4d319e6-66e4-4e72-b662-001a68233191)

#Codigo 2

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def max_de_tres(num1, num2, num3):

    return max(max(num1, num2), num3)

# Ejemplo de uso

resultado = max_de_tres(10, 20, 15)

print("El mayor es:", resultado)  # Debería imprimir: El mayor es: 20

![image](https://github.com/user-attachments/assets/f2316c6f-b1a6-4e26-ad9c-d10d99eaba36)

![image](https://github.com/user-attachments/assets/a6470755-ed75-42f2-bcb8-b9c40ade64b1)

#Codigo 3

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

![image](https://github.com/user-attachments/assets/29a4531a-c4c8-4ed0-932a-944d3d2e10ad)

![image](https://github.com/user-attachments/assets/3c6ab796-0912-4492-8595-68e0e1677375)

#Codigo 4

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

caracter=input("Ingresa una palabra:")

def es_vocal(caracter):

    # Convertimos el carácter a minúscula para manejar tanto mayúsculas como minúsculas
    
    caracter = caracter.lower()
    
    # Verificamos si el carácter es una vocal
    
    return caracter in "aeiou" 

  ![image](https://github.com/user-attachments/assets/dcd05153-a50c-46b1-9eb8-f7ff4b50d8d3)

![image](https://github.com/user-attachments/assets/e3b8cd98-e857-46a5-93e6-a4d05290b04e)

#Codigo 5

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

![image](https://github.com/user-attachments/assets/824373ee-e83a-4c5c-ad2b-aeede58f5350)

![image](https://github.com/user-attachments/assets/1f241513-1460-408c-abdc-a13d2f4196af)

#Codigo 6

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def inversa(cadena):

    return cadena[::-1]

# Ejemplo de uso

resultado = inversa("estoy probando")

print(resultado)  # Debería imprimir "odnaborp yotse"

![image](https://github.com/user-attachments/assets/ce015f20-219e-4725-b5d2-87347226b535)

![image](https://github.com/user-attachments/assets/ab04565d-fca9-492a-8a02-18422dcc58ae)

#Codigo 7

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

![image](https://github.com/user-attachments/assets/f83feaf6-97cc-48bb-b629-52d98890efab)

![image](https://github.com/user-attachments/assets/d2fbdfa7-4379-48a5-947b-813cf99c2198)

#codigo 8

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def superposicion(lista1, lista2):

    for elemento1 in lista1:
    
        for elemento2 in lista2:
        
            if elemento1 == elemento2:
            
                return True
                
    return False

![image](https://github.com/user-attachments/assets/d72cb2aa-7975-4f2e-8cfa-31a2875360a9)

![image](https://github.com/user-attachments/assets/5730b5f4-5594-4af5-b3a3-b09a04dd2d92)

#Codigo 9

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def generar_n_caracteres(n, caracter):

    return caracter * n

![image](https://github.com/user-attachments/assets/524e6a7b-4edf-4771-b123-f223ed43a2d1)

![image](https://github.com/user-attachments/assets/0d2d4223-d19b-4a5f-b24c-754357f7949d)

#Codigo 10

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

def procedimiento(lista):

    for numero in lista:
    
        print('*' * numero)

# Ejemplo de uso

procedimiento([4, 9, 7])

![image](https://github.com/user-attachments/assets/3c2828b6-4259-494d-81ae-47f6611c8471)

![image](https://github.com/user-attachments/assets/6881445a-c5f3-4676-a846-147ad1ad4aa9)

