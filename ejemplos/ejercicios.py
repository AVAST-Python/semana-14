# -----------------------------------------------------------------------------
# Sumar los elementos de una lista
# -----------------------------------------------------------------------------
def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(numeros)
print("La suma de la lista es:", resultado)


# -----------------------------------------------------------------------------
# Calcular la potencia de un número
# -----------------------------------------------------------------------------
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo de uso:
base = 2
exponente = 3
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")

# -----------------------------------------------------------------------------
# Verificar si todos los elementos de una lista son iguales
# -----------------------------------------------------------------------------
def todos_iguales(lista):
    if len(lista) <= 1:
        return True
    else:
        return lista[0] == lista[1] and todos_iguales(lista[1:])

# Ejemplo de uso:
lista_1 = [3, 3, 3, 3, 3]
lista_2 = [1, 2, 3, 4, 5]
print("¿Todos los elementos en lista_1 son iguales?", todos_iguales(lista_1))
print("¿Todos los elementos en lista_2 son iguales?", todos_iguales(lista_2))

# -----------------------------------------------------------------------------
# Invertir una cadena de texto
# -----------------------------------------------------------------------------
def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

# Ejemplo de uso:
texto = "Python"
resultado = invertir_cadena(texto)
print("Cadena invertida:", resultado)

# -----------------------------------------------------------------------------
# Verificar si una cadena es un palíndromo
# -----------------------------------------------------------------------------
def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True
    else:
        if cadena[0] == cadena[-1]:
            return es_palindromo(cadena[1:-1])
        else:
            return False

# Ejemplo de uso:
palabra = "radar"
resultado = es_palindromo(palabra)
print(f"¿'{palabra}' es un palíndromo? {resultado}")
