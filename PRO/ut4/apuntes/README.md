<h2 align= 'center'>Apuntes de listas</h2>

## Principales algoritmos de programación de listas:

### Búsqueda Lineal
Busca un elemento en una lista recorriéndola desde el principio hasta el final.

```python
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1 
```
### Búsqueda binaria
Busca un elemento en una lista ordenada dividiendo repetidamente el rango de búsqueda a la mitad.

```python
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
```
### Ordenamiento por burbuja

Ordena una lista comparando y cambiando repetidamente los elementos adyacentes si están en el orden incorrecto.

```python
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
```

### Ordenamiento por selección:
Ordena una lista encontrando repetidamente el elemento mínimo (o máximo) de la lista no ordenada y colocándolo al principio (o al final).

```python
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

```

### Ordenamiento por inserción:

Ordena una lista construyendo gradualmente una lista ordenada, insertando cada nuevo elemento en su posición correcta.
```python
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista
```

### Ordenamiento Rápido (QUICKSORT)

Ordena una lista utilizando el enfoque de dividir y conquistar, seleccionando un pivote y particionando la lista en sublistas menores y mayores que el pivote.

```python
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)
```

### Encontrar duplicados

```python
def primer_duplicado(lista):
    vistos = []
    for elemento in lista:
        if elemento en vistos:
            return elemento
        vistos.append(elemento)
    return None

```

## Ejemplos útiles y sencillos de listas por comprensión

### Convertir una lista a entero:

```python
lista_int = [int(v) for v in lista_str]
```

### Maximo o mínimo (ejercicio *minmax*):
```python
max_v = [v for v in num <= target]
min_v = [v for v in num > target]
```
aquí es importante fijarse en el *max_v* y poner ```<=``` para que incluya el valor máximo

### Convertir una lista de cuadrados:

```python
cuadrados = [x**2 for x in range(1, 11)]
```

### Filtrar números pares:
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
```

### Crear una lista de pares ordenados:

```python
pares_ordenados = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]
```

### aplanar listas:

```python
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_aplanada = [elemento for sublista in listas_anidadas for elemento in sublista]
```

### Palabras que empiezan por una letra:

```python
palabras = ["apple", "banana", "cherry", "avocado", "grape"]
empiezan_con_a = [palabra for palabra in palabras if palabra.startswith('a')]
```

### Devolver una lista con la longitud de las palabras:

```python
palabras = ["apple", "banana", "cherry", "date"]
longitudes = [len(palabra) for palabra in palabras]
```


### Crear una lista de números negativos:

Dada una lista solo devolver los negativos
```python
numeros = [1, -2, 3, -4, 5, -6]
negativos = [x for x in numeros if x < 0]

```
