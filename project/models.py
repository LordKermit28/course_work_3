from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(120), unique=True, nullable=True)

class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=True)
    description = Column(String(500))
    trailer = Column(String)
    year = Column(String)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genres.id"))

    genres = relationship("Genre")

    director_id = Column(Integer, ForeignKey("directors.id"))

    directors = relationship("Director")

class User(models.Base):
    __tablename__ = "users"

    email = Column(String(120), unique=True)
    password = Column(String(120))
    name = Column(String)
    surname = Column(String)
    favorite_genre = Column(Integer, ForeignKey("genres.id"))

    favorite_genres = relationship("Genre")




