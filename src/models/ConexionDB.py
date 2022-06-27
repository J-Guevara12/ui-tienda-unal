from urllib import request
import json

class ConexionDB:
    def __init__(self,url):
        self.url = url

    def ejecutar(self,accion):
        flujo = request.urlopen(self.url+accion)
        return json.loads(flujo.read())
