from flask_restx import Resource, Namespace
from impl import movie_service
from dao.models.movies import MovieSchema
from flask import request
from dao.models.directors import Director
from dao.models.genres import Genre
from dao.models.movies import Movie

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        genre_id = (request.args.get('genre_id'))
        if genre_id:
            objs = movie_service.filter_genre(int(genre_id))
            return MovieSchema(many=True).dump(objs)
        director_id = (request.args.get('director_id'))
        if director_id:
            objs = movie_service.filter_dir(director_id)
            return MovieSchema(many=True).dump(objs)
        year = (request.args.get('year'))
        if year:
            objs = movie_service.filter_year(year)
            return MovieSchema(many=True).dump(objs)
        objs = movie_service.get_all()
        return MovieSchema(many=True).dump(objs)

    def post(self):
        obj = movie_service.create(request.json)
        return MovieSchema().dump(obj), 201, {'location': f'/genre/{obj.id}'}


@movie_ns.route('/<int:pk>')
class MoviesView(Resource):
    def get(self, pk):
        obj = movie_service.get_one(pk)
        return MovieSchema().dump(obj)

    def delete(self, pk):
        movie_service.delete(pk)
        return 'удалено'

    def update(self, pk):
        obj = movie_service.update(pk, request.json)
        return MovieSchema().dump(obj)
