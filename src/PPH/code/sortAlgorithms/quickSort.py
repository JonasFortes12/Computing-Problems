#  o algoritmo Quick Sort escolhe um pivô, divide os elementos em duas partições com 
#  base nas razões calculadas usando a função ratio(arr[j]), ordena recursivamente as 
#  partições e, finalmente, combina as partições ordenadas com o pivô para obter a 
#  lista ordenada em ordem decrescente.

from code.ratio import ratio

def quickSortByRatio(arr):
    if len(arr) <= 1:
        return arr

    # Escolhe o pivô como o elemento do meio
    middle = len(arr) // 2
    pivot = arr[middle]

    # Divide os elementos em duas partições - menores e maiores que o pivô
    left = []
    right = []

    for i in range(len(arr)):
        if i == middle:
            continue
        if ratio(arr[i]) > ratio(pivot):
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Recursivamente ordena as partições
    sorted_left = quickSortByRatio(left)
    sorted_right = quickSortByRatio(right)

    # Combina as partições ordenadas com o pivô no meio
    return sorted_left + [pivot] + sorted_right