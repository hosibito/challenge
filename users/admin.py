from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CostomUserAdmin(UserAdmin):
    """Custom User Admin"""

    list_display = UserAdmin.list_display + (
        "language",
        "preference",
       
    )

    list_filter = UserAdmin.list_filter + (
        "language",
        "preference",
        "favourite_book_genre",
        "favourite_movie_genre",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "h_Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favourite_book_genre",
                    "favourite_movie_genre"
                ),
            },
        ),
    )


'''
@admin.register(User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + ((
        "Custom Profile",
        {
            "fields": (
                "bio",
                "preference",
                "language",
                "fav_book_genre",
                "fav_movie_genre",
            )
        },
    ), )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )

    list_filter = (
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )

'''
