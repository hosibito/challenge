import random
from django.core.management.base import BaseCommand

from django_seed import Seed

from users import models as users_models
from categories import models as categories_models

NAME = "users"


class Command(BaseCommand):  # 노트 9 참조
    help = f"{NAME} 더미데이터 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            default=1,
            type=int,
            help=f'{NAME}을/를 number 만큼 생성합니다.',
        )

    def handle(self, *args, **options):
        number = options.get("total")
        seeder = Seed.seeder()
        fav_book_categories = categories_models.Category.objects.filter(kind="book")
        fav_movie_categories = categories_models.Category.objects.filter(kind="movie")
        seeder.add_entity(
            users_models.User,
            number,
            {
                "is_staff": False, 
                "is_superuser": False, 
                "preference": lambda x: random.choice(["books","movies"]),
                "language": lambda x: random.choice(["english","korean"]),
                "fav_book_cat": lambda x: random.choice(fav_book_categories),
                "fav_movie_cat": lambda x: random.choice(fav_movie_categories),
            }
        )
        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"{number} {NAME} created!!")
        )
