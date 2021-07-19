import random
from django.core.management.base import BaseCommand

from django_seed import Seed

from reviews import models as reviews_models
from users import models as users_models
from movies import models as movies_models
from books import models as books_models

NAME = "reviews"

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
        all_users = users_models.User.objects.all()
        all_movies = movies_models.Movie.objects.all()
        all_books = books_models.Book.objects.all()
        
        seeder.add_entity(
            reviews_models.Review,
            number,
            {
                "created_by": lambda x: random.choice(all_users),
                "movie": lambda x: random.choice(all_movies),
                "book": lambda x: random.choice(all_books),
                "rating": lambda x: random.randint(1, 6),                
            }
        )
        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"{number} {NAME} created!!")
        )
