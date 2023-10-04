
# Recebe o conjunto (tupla) S de pares ordenados
def setMaximizeRatio(S):   
    
    # Inicializar as variáveis do problema
    S_asterisk = [S[0]]
    numerator = S[0][0]
    denominator = S[0][1]
    maxRatio = numerator/denominator
    
    
    # Iterar no conjunto S e selecionar os elementos que maximizam a razão entre sum(a) e sum(b)
    # de acordo com o lemma R(S*) = R*
    for i in range(1,len(S)):
        ratio = S[i][0]/S[i][1]
    
        if(ratio > maxRatio): 
            numerator += S[i][0]
            denominator += S[i][1]
            maxRatio = numerator/denominator
            S_asterisk.append(S[i])
                
               
            
    return S_asterisk
    
  
    
