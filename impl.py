from dao.directordao import DirectorDAO
from dao.genredao import GenreDAO
from dao.moviedao import MovieDAO
from servise.directordao import DirectorServise
from servise.genredao import GenreServise
from servise.moviedao import MovieServise
from setup_db import db

genre_dao = GenreDAO(db.session)
genre_service = GenreServise(dao=genre_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieServise(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorServise(dao=director_dao)
