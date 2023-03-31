from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc

from project.dao.base import BaseDAO
from project.models import Genre
from project.models import Director
from project.models import Movie
from werkzeug.exceptions import NotFound


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class DirectorDAO(BaseDAO[Director]):
    __model__ = Director

class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_by_filter(self, page, status):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if status == "new":
            stmt = stmt.order_by(desc(self.__model__.year))
        else:
            stmt = stmt.order_by(self.__model__.year)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()



