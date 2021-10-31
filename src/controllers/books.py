from flask import Flask,request,jsonify,make_response
from flask_restx import Api, Resource

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

@app.route('/books/<id>', methods=['GET'])
def book_search(id):
    resultBook = {}
    for book in books_db:
        if(book['id'] == int(id)):
            resultBook = book
            break           
    resultado = resultBook
    resposta = make_response(jsonify([resultado]),200)
    resposta.headers['Access-Control-Allow-Origin'] = '*'
    return resposta

@app.route('/books/<title>', methods=['GET'])
def book_search(title):
    resultBook = {}
    for book in books_db:
        if(book['title'] == title):
            resultBook = book
            break           
    resultado = resultBook
    resposta = make_response(jsonify([resultado]),200)
    resposta.headers['Access-Control-Allow-Origin'] = '*'
    return resposta    