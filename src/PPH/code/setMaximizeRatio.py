
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
    
  

def pph_algorithm(a, b):
    R = a[0] / b[0] # a0/b0 maior valor até o momento
    S_indice = [0] # guarda os indices de a e b.

    for k in range(1, len(a)-1): # os outros valores de a1,b1 a an,bn   
        # Testa ak/bk > R*
        resutado_k = a[k] / b[k] 

        # Verificar o funcionamento
        # print('k:', k)
        # print('r:', resutado_k)
        # print('s:', S_indice)
        # print("\n")

        if resutado_k > R:
            S_indice.append(k) # armazena o indice de n
            R = resutado_k # R é o maior até o momento
        

        for i in S_indice:
            
            if a[i] / b[i] < R:
                S_indice.remove(i)

    return S_indice, R


# a = [334, 272, 249]
# b = [149, 376, 372]

# a = [334,272,249,74,188,186,77,263,323,100,132]
# b = [265,923,20,260,434,563,874,581,84,743, 820]

a = [21 ,474 ,18,468,212,19, 379,41, 143,226,446]
b = [707,875,236,860,786,967,678,330,106,174,591]

s, r = pph_algorithm(a,b)

print(s)
print(r)
