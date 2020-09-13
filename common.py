import yaml


__config = None #Variable que nos servira para cachear nuestra configuracion.


def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f: #Abrimos el archivo config en modo de lectura
            __config = yaml.load(f)

    return __config
