from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Adam Sendler'),
})


movie: Model = api.model('Кино', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Побег из Шоушенко'),
    'description': fields.String(required=True, max_length=500),
    'trailer': fields.String(required=True),
    'year': fields.String(required=True),
    'rating': fields.Float(required=True),
    'genre_id': fields.Integer(required=True),
    'director_id': fields.Integer(required=True),
})

auth: Model = api.model('Авторизация', {
    'email': fields.String(required=True, example='Test'),
    'password': fields.String(required=True, example='21fsd'),
})

auth_result: Model = api.model('', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True),
})