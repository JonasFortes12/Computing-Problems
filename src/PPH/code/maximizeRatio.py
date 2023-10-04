def maximizeRatio(S):
    
    def verifyRatio(element, maxCurrentRatio):
        ratio = element[0]/element[1]
        if(ratio > maxCurrentRatio): 
            numerator += element[0]
            denominator += element[1]
            maxRatio = numerator/denominator
            S_asterisk.append(S[i])
            back = True
            return maxRatio
        else:
            return maxCurrentRatio

    # Inicializar as variáveis do problema
    S_asterisk = [S[0]]
    numerator = S[0][0]
    denominator = S[0][1]
    maxRatio = numerator/denominator
    
    # Iterar no conjunto S e selecionar os elementos que maximizam a razão entre sum(a) e sum(b)
    # de acordo com o lemma R(S*) = R*
    for i in range(1,len(S)):
        
        maxRatio = verifyRatio(S[i], maxRatio)
        
        
                
               
            
    return S_asterisk


# Esse código tá uma porcaria