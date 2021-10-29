from flask import Flask
from flask_restx import Api,Resource

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version = '1.0',
            title = 'Processamento de dados',
            description = 'Processamento de dados de um base de crédito',
            doc = '/docs'
        )
        def run(self, ):
            self.app.run(
                debug = True
            )    

server = Server()