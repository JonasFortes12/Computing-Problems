import os

def listFiles():
    instancias = {}
    for tipoDados in os.listdir('./AGM'):
        instancias[tipoDados] = os.listdir(os.path.join('./AGM', tipoDados))
    return instancias