import os

def listFiles():
    instancias = {}
    for tipoDados in os.listdir(os.path.join(os.path.dirname(__file__), 'AGM')):
        instancias[tipoDados] = os.listdir(os.path.join(os.path.dirname(__file__), 'AGM', tipoDados))
    return instancias




