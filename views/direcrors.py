from flask_restx import Resource, Namespace
from impl import director_servise
from dao.models.directors import DirectorSchema
from flask import request
director_ns = Namespace('directors')

@director_ns.route('/')
class GenresView(Resource):
    def get(self):
        objs = director_servise.get_all()
        return DirectorSchema(many=True).dump(objs)

    def post(self):
        obj = director_servise.create(request.json)
        return DirectorSchema().dump(obj), 201, {'location':f'/genre/{obj.id}'}


@director_ns.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        obj = director_servise.get_one(pk)
        return DirectorSchema().dump(obj)

    def delete(self, pk):
        director_servise.delete(pk)
        return 'удалено'

    def update(self, pk):
        obj = director_servise.update(pk, request.json)
        return DirectorSchema().dump(obj)
