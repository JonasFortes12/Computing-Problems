import random
import os

def main(lista):
    lista_instancias = []
    qtd_instancias = len(lista)
    for i in range(qtd_instancias):
        tuplas = []
        for j in range(lista[i]):
            tupla_int = (random.randint(1, 100), random.randint(1, 10))
            tuplas.append(tupla_int)
        lista_instancias.append(tuplas)


    for instancia in range(qtd_instancias):
        arquivo = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),f"instancia_{lista[instancia]}.txt"), "w")
        arquivo.write(str(lista_instancias[instancia]))
        arquivo.close()

lista = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 1000000, 5000000, 10000000]
main(lista)