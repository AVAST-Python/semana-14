def imprimir_numeros_recursivo(n):
    if n > 0:
        imprimir_numeros_recursivo(n - 1)  # Llamada recursiva con n-1
        print(n)  # Imprime el número actual

# Llamamos a la función con n=10 para imprimir los números del 1 al 10
imprimir_numeros_recursivo(10)



def encontrar_maximo_recursivo(lista):
    # Caso base: si la lista tiene un solo elemento, ese es el máximo
    if len(lista) == 1:
        return lista[0]

    # Recursión para encontrar el máximo en el resto de la lista
    resto_max = encontrar_maximo_recursivo(lista[1:])

    # Comparar el primer elemento con el máximo del resto de la lista
    return max(lista[0], resto_max)

# Ejemplo de uso:
numeros = [3, 8, 1, 10, 50, 7]
print(encontrar_maximo_recursivo(numeros))
