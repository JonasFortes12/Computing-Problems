import re

def loadpphData(file_path):
    data = []
    
    with open(file_path, 'r') as file:
        # Lê a quantidade de pares ordenados (n)
        n = int(file.readline().strip())
        
        # Inicializa as listas para os valores (a,b)
        allValues = []
        values_a = []
        values_b = []
        
        rows = file.readlines()
        for row in rows:
            values = re.findall(r'\d+\.\d+|\d+', row)
            for value in values:
                allValues.append(int(value))
        
        
        values_a = allValues[0:n+1]
        values_b = allValues[n+1:len(allValues)]
      
        orderedPairs = [(a, b) for a, b in zip(values_a, values_b)]
        
        data.extend(orderedPairs)
    
    return data
