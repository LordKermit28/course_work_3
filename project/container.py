from project.dao import DirectorDAO, GenresDAO, MovieDAO
from project.dao.user import UserDAO
from project.services import GenresService
from project.services.auth_service import AuthService
from project.services.user_service import UserService
from project.setup.db import db
from project.setup.api.parsers import page_parser
from project.services import GenresService, DirectorsService, MoviesService


# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)