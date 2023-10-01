# Ordenação Decrescente do Bubble Sort. Ou seja, organizar as maiores razões entre a e b para 
# serem as primeiras da lista de pares ordenados (a,b)
 
def bubbleSortByRatio(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Set a flag for optimization
        swapped = False

        # Traverse the list from the beginning to the end, ignoring the already sorted last elements
        for j in range(0, n - i - 1):
            # Calculate the ratio a/b for a and b in the current tuple
            a, b = arr[j]
            ratio1 = a / b

            # Calculate the ratio a/b for a and b in the next tuple
            a, b = arr[j + 1]
            ratio2 = a / b

            # Compare the ratios and swap the tuples if the current ratio is less than the next
            if ratio1 < ratio2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped in this iteration, the list is sorted
        if not swapped:
            break
    
    return arr