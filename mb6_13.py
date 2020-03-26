#!/usr/local/bin/python3
from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import get, post, request
from bottle import template
from datetime import date

import mb6_13album
#Перед началом просмотра кода, прочитайте description.txt, букав там немножко

@route("/albums/all/")
def get_all_albums():
    """ покажем всех исполнителей и альбомы, вывод данных в веб-страничку """
    artists_ = mb6_13album.find_all_artists()
    if artists_:
        fields_={
                "title": "База альбомов",
                "header": "Список всех альбомов",
                "artists": []
            }
        for artist_ in artists_:
            albums_ = mb6_13album.find(artist_.artist,artist_.genre)
            field_ = []
            if albums_:
                for album_ in albums_:
                    field_.append((album_[0], album_[1], album_[2]))
                fields_["artists"].append([artist_.artist, field_, artist_[1], artist_.genre])
            else:
                return HTTPError(500,"Ошибка базы данных! Данные не найдены!")
        return template('simple_all.tpl', fields_)
    else:
        return HTTPError(500,"Ошибка базы данных! Данные не найдены!")

@route("/albums/<artist>")
def get_albums(artist):
    """ Вывод данных в веб-страничку по названиею исполнителя"""
    albums_ = mb6_13album.find(artist)
    if albums_:
        fields_ = {
            "title": "База альбомов",
            "header": artist,
            "contents": [],
            "count":len(albums_)
        }
        for album_ in albums_:
            fields_["contents"].append((album_[0], album_[1], album_[2]))        
        return template('simple.tpl', fields_)
    else:
        return HTTPError(500,"Такого исполнителя нет в базе")

@get("/albums/")
def enter_album():
    """
    Для ввода данных через форму, сначала выдадим форму GET- запросом
    """
    return template('input.tpl')

@post("/albums/")
def set_album():
    """ Получаем данные о новом альбоме методом POST и сохраняем в БД 
    !!! Обратите внимание !!!
    В задании 13.2 POST запросы в route /albums/ с закрывающим слешем"""
    album_data = {
        "artist": request.forms.artist.title(),
        "genre": request.forms.genre.title(),
        "album": request.forms.album,
        "year": request.forms.year
    }
    year_ = album_data["year"]
    #проверим введеный год, возьмем год из сегодняшней даты
    current_year_ = date.today()
    c_y_ = current_year_.isoformat()
    c_y_ = int(c_y_[0:c_y_.find("-")])

    try:
        #пробуем преобразовать в число, если введено не число, покажем ошибку
        y_ = int(year_)
    except ValueError:
        return HTTPError(409, "Неправильный формат года выпуска альбома, разрешены только числа!")
    try:
        #предположим, что до 1000 года н.э. точно не было альбомов, и альбом из будущего тоже не принимается
        if not (1000 < y_ <=c_y_):
            raise ValueError("Неправильный формат года, введите правильный календарный год!") #кидаем исключение
    except ValueError as err:
        return HTTPError(409, err)

    if mb6_13album.check_album(album_data):
        return HTTPError(409, "Альбом уже есть в БД")
    else:
        if mb6_13album.write_db(album_data): #оставим задел, на случай, если в функции будет реализована дополнительная проверка
            return template("success.tpl",album_data)



if __name__ == "__main__":
    run(host="localhost", port=8080, debug = True)
