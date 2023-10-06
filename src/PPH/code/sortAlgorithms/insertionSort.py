# Esta função insertionSortByRatio irá ordenar o array arr de pares ordenados 
# em ordem decrescente com base nas razões a/b de cada par,
# usando o algoritmo de ordenação Insertion Sort.

from code.ratio import ratio 

def insertionSortByRatio(arr):
    # Obtém o comprimento do array
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(1, n):
        # Armazena o elemento atual para inserção posterior
        current = arr[i]

        # Obtém a razão a/b do elemento atual usando a função ratio
        current_ratio = ratio(current)

        # Move os elementos maiores que o elemento atual para a direita
        j = i - 1
        while j >= 0 and current_ratio > ratio(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1

        # Insere o elemento atual na posição correta
        arr[j + 1] = current

    return arr