from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': 'Alice no país das maravilhas' },
    {'id': 1, 'title': 'Alice por trás do espelho' },
    {'id': 2, 'title': 'Talvez você precise falar com alguém' }
]

@api.route('/books')
class BookList(Resource):
    def get(self, ):
        return books_db