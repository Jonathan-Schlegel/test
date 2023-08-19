from random import randint
import app_film.users as users
import app_film.data_processing as data_processing
import app_film.films as films

films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]


friends = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]

"""Création des amis"""
object_friends = []
for friend in friends:
    try:
        object_friends.append(users.User(friend[0],data_processing.Clean.get_film_friend(friend)))
    except  IndexError:
        object_friends.append(users.User(friend[0], ""))

"""Ensemble des films trié"""
virtual_libray = []

"""for film in films:
    print(type(data_processing.Clean.get_title(film)))
    print(type(data_processing.Clean.get_year(film)))
    print(type(data_processing.Clean.get_support(film)))
    if data_processing.Clean.get_support(film) == "DVD":
        virtual_libray.append(films.filmDVD(title = data_processing.Clean.get_title(film), year = data_processing.Clean.get_year(film)))
    else :
        virtual_libray.append(films.filmVHS(title = data_processing.Clean.get_title(film), year = data_processing.Clean.get_year(film)))
"""
#for film in virtual_libray:
#    print(film)
mon_film = ("Blade Runner (1982)", "vhf")
title = data_processing.Clean.get_title(mon_film)
year = data_processing.Clean.get_year(mon_film)
print(title, year)
print(films.filmVHS(title, year))
#virtual_libray.append(films.filmVHS(title = data_processing.Clean.get_title(mon_film), year = data_processing.Clean.get_year(mon_film)))
