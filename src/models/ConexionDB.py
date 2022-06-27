from urllib import request, parse
import requests
import json

class ConexionDB:
    def __init__(self,url):
        self.url = url

    def get(self,accion):
        flujo = request.urlopen(self.url+accion)
        return json.loads(flujo.read())

    def post(self,accion,data):
        data = parse.urlencode(data).encode('utf-8')
        #req =  request.Request(self.url+accion, data=data)
        resp = request.urlopen(self.url+accion, data=data)
        print(resp.info())
        return json.loads(resp.read())

conn = ConexionDB('http://127.0.0.1:5000')
data = {'usuario': '1002655778','contrasena': 123456}
