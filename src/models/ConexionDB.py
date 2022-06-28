from urllib import request, parse
import requests
import json

class ConexionDB:
    def __init__(self,url):
        self.url = url

    def get(self,accion):
        #flujo = request.urlopen(self.url+accion)
        #return json.loads(flujo.read())
        r = requests.get(self.url+accion)
        return r.json()

    def post(self,accion,data):
        r = requests.post(self.url+accion, json=data)
        return r.json()

    def put(self,accion,data):
        r = requests.put(self.url+accion, json=data)
        return r.json()

    def delete(self,accion,data):
        r = requests.delete(self.url+accion,json=data)
        return r.json()
