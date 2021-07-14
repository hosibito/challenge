from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIE = "movies"
    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, 'Books'),
        (PREFERENCE_MOVIE, 'Movies')
    )
    
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    GENRE_CHOICES = (
        ("추리", "추리"),
        ("모험", "모험"),
        ("판타지", "판타지"),
        ("SF", "SF"),
        ("로멘스", "로멘스"),
        ("게임", "게임"),
        ("사극", "사극"),
        ("스릴러", "스릴러"),
    )
    
    bio = models.TextField(blank=True)
    preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=6, default=PREFERENCE_BOOKS)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default=LANGUAGE_KOREAN)
    favourite_book_genre = models.CharField(choices=GENRE_CHOICES,  max_length=10, blank=True)  # 나중에 ManyToManyField 로 될듯
    favourite_movie_genre = models.CharField(choices=GENRE_CHOICES, max_length=10, blank=True) # 나중에 ManyToManyField 로 될듯


'''
class User(AbstractUser):
    
    PREF_BOOKS = "books"
    PREF_MOVIES = "movies"
    PREF_CHOICES = ((PREF_BOOKS, "Books"), (PREF_MOVIES, "Movies"))

    LANG_EN = "english"
    LANG_KR = "korean"
    LANG_CHOICES = (
      (LANG_EN, "English"),
      (LANG_KR, "Korean")
    )

    GENRE_ACTION = "action"
    GENRE_COMEDY = "comedy"
    GENRE_THRILLER = "thriller"
    GENRE_HISTORY = "history"

    GENRE_CHOICES = (
      (GENRE_ACTION, "Action"),
      (GENRE_COMEDY, "Comedy"),
      (GENRE_THRILLER, "Thriller"),
      (GENRE_HISTORY, "History"),
    )

    bio = models.TextField()
    preference = models.CharField(
        max_length=20, choices=PREF_CHOICES, default=PREF_MOVIES)
    language = models.CharField(
        max_length=20, choices=LANG_CHOICES, default=LANG_EN)
    fav_book_genre = models.CharField(
        max_length=20, choices=GENRE_CHOICES, default=GENRE_HISTORY)
    fav_movie_genre = models.CharField(
        max_length=20, choices=GENRE_CHOICES, default=GENRE_HISTORY)
'''