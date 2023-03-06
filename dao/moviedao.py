from dao.models.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Movie).get(pk)


    def get_all(self):
        return self.session.query(Movie).all()


    def create(self, data):
        obj = Movie(**data)
        self.session.add(obj)
        self.session.commit()

        return obj

    def delete(self, pk):
        obj = self.get_one(pk)
        self.session.delete(obj)
        self.session.commit()


    def update(self, pk, data):
        obj = self.get_one(pk)
        
        obj.title = data.get('title')
        obj.description = data.get('description')
        obj.trailer = data.get('trailer')
        obj.year = data.get('year')
        obj.rating = data.get('rating')

        self.session.add(obj)
        self.session.commit()
        return