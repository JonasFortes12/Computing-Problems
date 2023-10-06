# o algoritmo Merge Sort divide o array em duas metades, ordena cada metade recursivamente 
# e, em seguida, combina as duas metades ordenadas em ordem decrescente 
# com base nas razões calculadas

from code.ratio import ratio 

def mergeSortByRatio(arr):
    if len(arr) <= 1:
        return arr

    # Divide o array ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordena as metades
    left_half = mergeSortByRatio(left_half)
    right_half = mergeSortByRatio(right_half)

    # Combina as metades ordenadas
    sorted_arr = merge(left_half, right_half)

    return sorted_arr

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Combina as duas metades em ordem decrescente de acordo com a razão a/b
    while left_index < len(left) and right_index < len(right):
        if ratio(left[left_index]) > ratio(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes, se houver
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
