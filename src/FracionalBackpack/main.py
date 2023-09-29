from a import mochila_frac_n_log_n as mf_a
from b import mochila_frac_n as mf_b
from c import mochila_frac_n as mf_c
import os

dir_name = os.path.abspath(os.path.dirname(__file__))
n = 2

pasta = os.path.join(dir_name, 'instancias',f'instancia_{n}.txt' )

arquivo = open(pasta, "r")
conteudo = arquivo.read()
arquivo.close()
# Converter a string em uma lista de tuplas usando a função eval
arr = eval(conteudo)

m1, v1 = mf_a.construir_mochila(arr, 50)
m2, v2 = mf_b.construir_mochila(arr, 50)
m3, v3 = mf_c.construir_mochila(arr, 50)

print(m1,m2,m3)
print(v1,v2,v3)
