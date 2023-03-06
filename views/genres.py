from flask_restx import Api, Resource, Namespace
from impl import genre_servise
from dao.models.genres import GenrerSchema
from flask import request
genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        objs = genre_servise.get_all()
        return GenrerSchema(many=True).dump(objs)

    def post(self):
        obj = genre_servise.create(request.json)
        return GenrerSchema().dump(obj), 201, {'location':f'/genre/{obj.id}'}


@genre_ns.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        obj = genre_servise.get_one(pk)
        return GenrerSchema().dump(obj)

    def delete(self, pk):
        genre_servise.delete(pk)
        return 'удалено'

    def update(self, pk):
        obj = genre_servise.update(pk, request.json)
        return GenrerSchema().dump(obj)
