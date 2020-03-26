import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    структура таблицы album для хранения записей музыкальной библиотеки
    """
    __tablename__ = "album"
    id = sa.Column(sa.INTEGER, primary_key = True, autoincrement = True)
    year = sa.Column(sa.INTEGER, default = 1970)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def find_all_artists():
    """
    Находит всех исполнителей в базе данных
    чтобы избежать повторов группируем выборку по полю имя исполнителя
    и жанру, например, если рокер оскотинился и записал попсу 
    то попса пойдет отдельным жанром, чтобы не порочить рок,
    заодно считаем количество альбомов исполнителя
    """
    session = connect_db()
    artists = session.query(Album.artist, func.count(Album.artist), Album.genre).order_by(Album.artist.asc()).group_by(Album.artist).group_by(Album.genre).all()
    return artists

def find(artist, genre = None):
    """
    Находит все альбомы в базе данных по заданному артисту, для пробы вернем не объект, а список 
    """
    session = connect_db()
    if genre is None:
        albums = session.query(Album).filter(Album.artist == artist).order_by(Album.year.desc()).all()
    else:
        albums = session.query(Album).filter(Album.artist == artist).filter(Album.genre == genre).order_by(Album.year.desc()).all()
    return_ = [(album_.album,album_.genre,album_.year) for album_ in albums]
    session.close()
    return return_

def write_db(album):
    """
    Сохраняем исполнителя/альбом в базу, в album - словарь с полями для БД
    """
    session = connect_db()
    album_ = Album(year = album["year"], artist = album["artist"], genre = album["genre"], album = album["album"])
    session.add(album_)
    session.commit()
    return "Данные успешно сохранены"

def check_album(album_data):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == album_data["artist"]).filter(Album.album == album_data["album"]).count()
    return albums

def flush_session():
    #session.commit()
    return True