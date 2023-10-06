# algoritmo Heap Sort é usado para ordenar o array em ordem decrescente 
# com base nas razões calculadas usando a função ratio(arr[j]). 
# Ele primeiro constrói um heap máximo a partir do array e depois 
# extrai os elementos do heap um por um para obter a lista ordenada.

from code.ratio import ratio 

def heapify(arr, n, i):
    largest = i  # Inicializa o maior como raiz
    left = 2 * i + 1  # Índice do filho da esquerda
    right = 2 * i + 2  # Índice do filho da direita

    # Verifica se o filho da esquerda existe e é menor que a raiz
    if left < n and ratio(arr[left]) < ratio(arr[largest]):
        largest = left

    # Verifica se o filho da direita existe e é menor que a raiz
    if right < n and ratio(arr[right]) < ratio(arr[largest]):
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca a raiz com o maior
        heapify(arr, n, largest)  # Reorganiza a subárvore afetada

def heapSortByRatio(arr):
    n = len(arr)

    # Constrói um heap mínimo (ordem decrescente)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos do heap um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca o elemento máximo com o último
        heapify(arr, i, 0)  # Reorganiza a subárvore não classificada

    return arr
