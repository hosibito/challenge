import random

from django.core.management.base import BaseCommand
from django.db.models import Q
from django_seed import Seed

from books import models as books_models
from categories import models as categories_models
from people import models as people_models


NAME = "books"


class Command(BaseCommand):  # 노트 9 참조
    help = f"{NAME} 더미데이터 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            default=1,
            type=int,
            help=f'{NAME}을/를 total 만큼 생성합니다.',
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()     
        books_categories = categories_models.Category.objects.filter(Q(kind="book")|Q(kind="both"))
        writer_people = people_models.Person.objects.filter(kind="writer")        
        seeder.add_entity(
            books_models.Book,
            total,
            {
                "title": lambda x: seeder.faker.sentence(),  
                "year": lambda x: random.randint(1980, 2022), 
                "cover_image": lambda x:f"book/{random.randint(1, 17)}.webp",        
                "rating": lambda x: random.randint(1,6),
                "category": lambda x: random.choice(books_categories),
                "writer": lambda x: random.choice(writer_people),                             
            }
        )           
        seeder.execute()   

        self.stdout.write(
            self.style.SUCCESS(f"{total} {NAME} created!!")
        )
