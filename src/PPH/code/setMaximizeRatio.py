
# Recebe o conjunto (tupla) S de pares ordenados
def setMaximizeRatio(S):   
    
    # Inicializar as variáveis do problema
    S_asterisk = []
    maxRatio = 0
    numerator = 0
    denominator = 0
    
    # Iterar no conjunto S e selecionar os elementos que maximizam a razão entre sum(a) e sum(b)
    # de acordo com o lemma R(S*) = R*
    for i in range(len(S)):
        ratio = S[i][0]/S[i][1]
        
        if(ratio > maxRatio): 
            numerator += S[i][0]
            denominator += S[i][1]
            maxRatio = numerator/denominator
            S_asterisk.append(S[i])
            
    return S_asterisk
    
  
    
