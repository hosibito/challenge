import random

from django.core.management.base import BaseCommand
from django.db.models import Q
from django.contrib.admin.utils import flatten
from django_seed import Seed

from movies import models as movies_models
from categories import models as categories_models
from people import models as people_models


NAME = "movies"


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
        movie_categories = categories_models.Category.objects.filter(Q(kind="movie")|Q(kind="both"))
        director_people = people_models.Person.objects.filter(kind="director")
        actor_people = people_models.Person.objects.filter(kind="actor")
        seeder.add_entity(
            movies_models.Movie,
            total,
            {
                "title": lambda x: seeder.faker.sentence(),  
                "year": lambda x: random.randint(1980, 2022),              
                "rating": lambda x: random.randint(1,6),
                "category": lambda x: random.choice(movie_categories),
                "director": lambda x: random.choice(director_people),                             
            }
        )
           
        created_movies = seeder.execute()          
        created_movies_pk_clean = flatten(list(created_movies.values()))  

        for pk in created_movies_pk_clean:
            pk_movies = movies_models.Movie.objects.get(pk=pk)        
            for a_p in actor_people: 
                magic_number = random.randint(0, 15)
                if magic_number % 3 == 0:
                    pk_movies.cast.add(a_p)    

        self.stdout.write(
            self.style.SUCCESS(f"{total} {NAME} created!!")
        )
