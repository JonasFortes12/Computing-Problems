from modules import measureIt


# Este é um algoritmo de teste
def algorithm():
    i = 0
    for a in range(100000):
        for b in range(1000):
            i += 1

# Chamo a função que recebe o algoritmo e retorna a sua complexidade de tempo e espaço
print(measureIt.measureComplexity(algorithm, 'Algoritmo de teste'))