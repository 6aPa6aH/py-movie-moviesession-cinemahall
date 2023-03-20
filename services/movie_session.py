import datetime

from db.models import MovieSession
from django.db.models import QuerySet


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: datetime = None) -> QuerySet:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    queryset = MovieSession.objects.get(id=movie_session_id)
    return queryset


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    queryset = MovieSession.objects.filter(id=session_id)
    if show_time:
        queryset.update(show_time=show_time)

    if movie_id:
        queryset.update(movie_id=movie_id)

    if cinema_hall_id:
        queryset.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    queryset = MovieSession.objects.filter(id=session_id)
    queryset.delete()