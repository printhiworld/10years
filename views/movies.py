from flask_restx import Resource, Namespace
from impl import movie_servise
from dao.models.movies import MovieSchema
from flask import request
movie_ns = Namespace('movies')

@movie_ns.route('/')
class GenresView(Resource):
    def get(self):
        objs = movie_servise.get_all()
        return MovieSchema(many=True).dump(objs)

    def post(self):
        obj = movie_servise.create(request.json)
        return MovieSchema().dump(obj), 201, {'location':f'/genre/{obj.id}'}


@movie_ns.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        obj = movie_servise.get_one(pk)
        return MovieSchema().dump(obj)

    def delete(self, pk):
        movie_servise.delete(pk)
        return 'удалено'

    def update(self, pk):
        obj = movie_servise.update(pk, request.json)
        return MovieSchema().dump(obj)
