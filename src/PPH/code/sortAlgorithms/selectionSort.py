# a função ratio(arr[j]) é usada para calcular a razão a/b para cada par ordenado, 
# e o algoritmo Selection Sort é usado para ordenar o array em ordem decrescente 
# com base nas razões calculadas.

from code.ratio import ratio 

def selectionSortByRatio(arr):
    # Obtém o comprimento do array
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n - 1):
        # Encontra o índice do máximo elemento na parte não ordenada
        max_index = i
        for j in range(i + 1, n):
            if ratio(arr[j]) > ratio(arr[max_index]):
                max_index = j

        # Troca o máximo elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr