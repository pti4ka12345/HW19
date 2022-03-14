from HW19.dao.director import DirectorDAO
from HW19.dao.genre import GenreDAO
from HW19.dao.movie import MovieDAO
from HW19.dao.user import UserDAO
from HW19.service.director import DirectorService
from HW19.service.genre import GenreService
from HW19.service.movie import MovieService
from HW19.service.user import UserService
from HW19.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
