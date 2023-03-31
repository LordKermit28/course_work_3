from typing import Optional

from project.exceptions import ItemNotFound
from project.models import Movie
from project.dao.main import MovieDAO

class MoviesService:
    def __init__(self, dao: MovieDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> list[Movie]:
        return self.dao.get_by_filter(page=page, status=status)


