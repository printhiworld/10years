from dao.models.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Genre).get(pk)


    def get_all(self):
        return self.session.query(Genre).all()


    def create(self, data):
        obj = Genre(**data)
        self.session.add(obj)
        self.session.commit()

        return obj

    def delete(self, pk):
        obj = self.get_one(pk)
        self.session.delete(obj)
        self.session.commit()


    def update(self, pk, data):
        obj = self.get_one(pk)
        obj.name = data.get('name')
        self.session.add(obj)
        self.session.commit()
        return