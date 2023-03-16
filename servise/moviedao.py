from dao.models.movies import MovieSchema
movie_schema = MovieSchema()
class MovieServise:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, pk):
        self.dao.get_one(pk)

    def filter_year(self, year):
        obj = self.dao.filter_year(year)
        return obj
    def filter_dir(self, dir_id):
        obj = self.dao.filter_dir(dir_id)
        return obj
    def filter_genre(self, gen_id):
        obj = self.dao.filter_genre(gen_id)
        return obj

    def create(self, data):
        return self.dao.create(data)

    def delete(self, pk):
        return self.dao.delete(pk)

    def update(self, pk, data):
        return self.dao.update(pk, data)