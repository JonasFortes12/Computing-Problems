# Ordenação Decrescente do Bubble Sort. Ou seja, organizar as maiores razões entre a e b para 
# serem as primeiras da lista de pares ordenados (a,b)

from code.ratio import ratio 

def bubbleSortByRatio(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Set a flag for optimization
        swapped = False

        # Traverse the list from the beginning to the end, ignoring the already sorted last elements
        for j in range(0, n - i - 1):
            
            # Compare the ratios and swap the tuples if the current ratio is less than the next
            if ratio(arr[j]) < ratio(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped in this iteration, the list is sorted
        if not swapped:
            break

    return arr

# # Exemplo de uso:
# sorted_pairs = bubbleSortByRatio([(1, 1), (1, 2), (2, 1)])
# print(sorted_pairs)